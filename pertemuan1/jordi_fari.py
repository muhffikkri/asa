def get_sum(pic, r, c, size):
    total = 0
    for i in range(r, r + size):
        for j in range(c, c + size):
            total += pic[i][j]
    return total

def main():
    line1 = input().split()
    n_rows = int(line1[0])
    m_cols = int(line1[1])
        
    pic = []
    for _ in range(n_rows):
        pic.append(list(map(int, input().split())))

    pic_best_quality = -float('inf') 
    pic_best_size = 0
    pic_best_pos_x = 0
    pic_best_pos_y = 0

    for size in range(1, min(n_rows, m_cols) + 1):
        
        for r in range(n_rows - size + 1):
            for c in range(m_cols - size + 1):
                
                current_quality = get_sum(pic, r, c, size)
                is_better = False
                
                if current_quality > pic_best_quality:
                    is_better = True 
                elif current_quality == pic_best_quality:
                    if size > pic_best_size:
                        is_better = True 
                    elif size == pic_best_size:
                        if (r + 1) < pic_best_pos_x:
                            is_better = True
                        elif (r + 1) == pic_best_pos_x:
                            if (c + 1) < pic_best_pos_y:
                                is_better = True 
                
                if is_better:
                    pic_best_quality = current_quality
                    pic_best_size = size
                    pic_best_pos_x = r + 1 
                    pic_best_pos_y = c + 1

    print(f"{pic_best_quality} {pic_best_size} {pic_best_pos_x} {pic_best_pos_y}")

main()