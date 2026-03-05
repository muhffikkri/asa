# Nama : Muhammad Fikri 
# NIM  : 24060124130069
# Lab  : A2

def position_attempt(row, n, data_pos, queen_pos):
    if row == n:
        return True

    for col in range(n):
        if col in data_pos[0] or (row + col) in data_pos[1] or (row - col) in data_pos[2]:
            continue

        queen_pos[row][col] = "Q"
        data_pos[0].add(col)
        data_pos[1].add(row + col)
        data_pos[2].add(row - col)

        if position_attempt(row + 1, n, data_pos, queen_pos):
            return True

        queen_pos[row][col] = "."
        data_pos[0].remove(col)
        data_pos[1].remove(row + col)
        data_pos[2].remove(row - col)

    return False

def main():
    n_input = input().strip()
    n = int(n_input)
    
    data_pos = [set(), set(), set()]
    queen_pos = [["."] * n for _ in range(n)]

    if position_attempt(0, n, data_pos, queen_pos):
        result = "\n".join(["".join(baris) for baris in queen_pos])
        print(result)
    else:
        print("Kerajaan tidak dapat dilindungi!")
        

main()