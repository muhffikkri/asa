# Nama : Muhammad Fikri 
# NIM  : 24060124130069
# Lab  : A2

def main():
    r, c, d = list(map(int, input().split()))
    matrix = []
    for _ in range(r):
        row = list(map(int, input().split()))
        matrix.append(row)

    max_suhu = -1

    for row_shift in range(r - 2): 
        for col_shift in range(c - 2):
            upper_bound = -1
            lower_bound = 1000001 # Suhu max di constraints adalah 10^6
            total = 0
            
            for i in range(row_shift, row_shift + 3):
                for j in range(col_shift, col_shift + 3):
                    val = matrix[i][j]
                    
                    if val > upper_bound:
                        upper_bound = val
                    if val < lower_bound:
                        lower_bound = val
                    total += val
            
            range_suhu = upper_bound - lower_bound
            
            if range_suhu >= d: 
                if total > max_suhu:
                    max_suhu = total
    
    print(max_suhu)

main()