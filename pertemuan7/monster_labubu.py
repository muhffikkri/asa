def main():
    n, m = map(int, input().split())
    
    spatial_matrix = []
    for _ in range(n):
        val = list(map(int, input().split()))
        spatial_matrix.append(val)

    visited = [[False for _ in range(m)] for _ in range(n)]
    hiding_spot_count = 0

    for i in range(n):
        for j in range(m):
            if spatial_matrix[i][j] == 1 and not visited[i][j]:
                stack = [(i, j)]
                visited[i][j] = True
                component_size = 0
                
                while stack:
                    row, col = stack.pop()
                    component_size += 1
                    
                    for delta_row, delta_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        new_row, new_col = row + delta_row, col + delta_col
                        
                        if 0 <= new_row < n and 0 <= new_col < m:
                            if spatial_matrix[new_row][new_col] == 1 and not visited[new_row][new_col]:
                                visited[new_row][new_col] = True
                                stack.append((new_row, new_col))
                
                if component_size >= 2:
                    hiding_spot_count += 1

    print(hiding_spot_count)

main()