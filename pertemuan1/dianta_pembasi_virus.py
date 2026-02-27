def get_sum(virus, r, c, size):
    total = virus[r][c]
    for i in range(0, size):
        if i == c : continue
        total += virus[i][c]
    for j in range(0, size):
        if j == r : continue
        total += virus[r][j]
    return total

def main() : 
    line1 = input().split()
    n = int(line1[0])
        
    virus = []
    for _ in range(n):
        virus.append(list(map(int, input().split())))

    virus_cure_max_qty = 0
    virus_best_pos_x = 0
    virus_best_pos_y = 0

    for r in range(0, n) : 
        for c in range(0, n) : 
            current_cure_qty = get_sum(virus, r, c, n)
            is_better = False
                
            if current_cure_qty > virus_cure_max_qty:
                is_better = True 
            elif current_cure_qty == virus_cure_max_qty:
                if (r + 1) < virus_best_pos_x:
                    is_better = True
                elif (r + 1) == virus_best_pos_x:
                    if (c + 1) <= virus_best_pos_y:
                        is_better = True 
                
            if is_better:
                virus_cure_max_qty = current_cure_qty
                virus_best_pos_x = r + 1 
                virus_best_pos_y = c + 1

    print(f"{virus_cure_max_qty} {virus_best_pos_x} {virus_best_pos_y}")

main()