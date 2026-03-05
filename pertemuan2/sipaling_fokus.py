# Pembuat      : Muhammad Fikri / 24060124130069
# Tanggal      : 1 Maret 2026

def main():
    n, time_limit = list(map(int, input().split()))

    songs = []
    for _ in range(n):
        song_duration, song_focus = list(map(int, input().split()))
        if song_duration < 5: 
            songs.append((song_duration, song_focus))

    if len(songs) == 0:
        print(0)
        return

    focus_max = 0

    combination = [[-1] * len(songs) for _ in range(time_limit + 1)]

    for i in range(len(songs)):
        duration, focus = songs[i]
        if duration <= time_limit:
            combination[duration][i] = focus

    for t in range(1, time_limit + 1):
        for i in range(len(songs)):
            if combination[t][i] == -1: continue

            for j in range(len(songs)):
                if i == j: continue

                next_duration, next_focus = songs[j]
                if t + next_duration <= time_limit:
                    new_focus = combination[t][i] + next_focus
                    if new_focus > combination[t + next_duration][j]: combination[t + next_duration][j] = new_focus

    for playlist in combination :
        focus_max = max(focus_max, max(playlist))        
    for i in range(time_limit + 1): 
        for j in range(len(songs)):
            if combination[i][j] > focus_max:
                focus_max = combination[i][j]
    print(focus_max)

main()