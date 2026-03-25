# Nama : Muhammad Fikri
# NIM : 24060124130069
# Lab : A2

def main():
    n, m = map(int, input().split())
    fi = list(map(int, input().split()))
    
    all_rooms = []
    while len(all_rooms) < m:
        room = input().split()
        if not room: break
        all_rooms.extend(map(int, room))

    prefix_sum = [0] * n
    prefix_sum[0] = fi[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + fi[i]

    results = []
    for room_num in all_rooms:
        low = 0
        high = n - 1
        floor_idx = 0
        
        while low <= high:
            mid = (low + high) // 2
            if prefix_sum[mid] >= room_num:
                floor_idx = mid
                high = mid - 1 
            else:
                low = mid + 1  
        
        if floor_idx == 0:
            room_in_floor = room_num
        else:
            room_in_floor = room_num - prefix_sum[floor_idx - 1]
            
        results.append(str(floor_idx + 1) + " " + str(room_in_floor))

    print("\n".join(results))

main()