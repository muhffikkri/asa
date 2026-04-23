def main():
    n, m = map(int, input().split())
    
    spatial_matrix = []
    for _ in range(n):
        val = list(map(int, input().split()))
        spatial_matrix.append(val)

    visited = [[False for _ in range(m)] for _ in range(n)]
    
    lake_count = 0
    river_count = 0

    for i in range(n):
        for j in range(m):
            if spatial_matrix[i][j] == 0 and not visited[i][j]:
                is_river = False
                queue = [(i, j)]
                visited[i][j] = True
                
                head = 0
                while head < len(queue):
                    row, col = queue[head]
                    head += 1
                    
                    if row == 0 or row == n - 1 or col == 0 or col == m - 1:
                        is_river = True
                    
                    for delta_row, delta_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        new_row, new_col = row + delta_row, col + delta_col
                        
                        if 0 <= new_row < n and 0 <= new_col < m:
                            if spatial_matrix[new_row][new_col] == 0 and not visited[new_row][new_col]:
                                visited[new_row][new_col] = True
                                queue.append((new_row, new_col))
                
                if is_river:
                    river_count += 1
                else:
                    lake_count += 1

    print(lake_count, river_count)

main()