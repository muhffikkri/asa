# Pembuat      : Muhammad Fikri / 24060124130069
# Tanggal      : 28 Februari 2026
 
def get_sum(virus, r, c, t, n):
    total = 0
    for i in range(max(0, r - t), min(n, r + t + 1)):
        remaining_dist = t - abs(r - i)
        
        col_start = max(0, c - remaining_dist)
        col_end = min(n, c + remaining_dist + 1)
        
        for j in range(col_start, col_end):
            total += virus[i][j]
    return total

def main() : 
    constraint = input().split()
    n = int(constraint[0])
    t = int(constraint[1])
        
    virus = []
    for _ in range(n):
        virus.append(list(map(int, input().split())))

    virus_cure_max_qty = -1
    virus_best_pos_x = 0
    virus_best_pos_y = 0

    for r in range(0, n) : 
        for c in range(0, n) : 
            current_cure_qty = get_sum(virus, r, c, t, n)
            is_better = False
                
            if current_cure_qty > virus_cure_max_qty:
                is_better = True 
            elif current_cure_qty == virus_cure_max_qty:
                if (r + 1) < virus_best_pos_x:
                    is_better = True
                elif (r + 1) == virus_best_pos_x:
                    if (c + 1) < virus_best_pos_y:
                        is_better = True 
                
            if is_better:
                virus_cure_max_qty = current_cure_qty
                virus_best_pos_x = r + 1 
                virus_best_pos_y = c + 1

    print(f"{virus_cure_max_qty} {virus_best_pos_x} {virus_best_pos_y}")

main()