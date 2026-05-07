def main():
    n, m = map(int, input().split())
    sx, sy, gx, gy = map(int, input().split())
    
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))

    # Min_dist mencatat total bahaya minimum ke tiap sel
    min_dist = [[float('inf')] * m for _ in range(n)]
    min_dist[sx][sy] = 0 # Nilai sel awal tidak dihitung
    
    queue = [(sx, sy, 0)]
    
    while queue:
        x, y, current_danger = queue.pop(0)
        
        # Cek 4 arah gerakan
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] >= 0:
                new_danger = current_danger + grid[nx][ny]
                if new_danger < min_dist[nx][ny]:
                    min_dist[nx][ny] = new_danger
                    queue.append((nx, ny, new_danger))

    result = min_dist[gx][gy]
    print(result if result != float('inf') else -1)

if __name__ == "__main__":
    main()