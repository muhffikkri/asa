def main():
    n, m = map(int, input().split())
    r, c = map(int, input().split())

    grid = [[-1 for _ in range(m)] for _ in range(n)]
    path = []

    def solve(curr_r, curr_c, step):
        grid[curr_r][curr_c] = step
        path.append((curr_r, curr_c))

        if step == n * m:
            return True

        directions = [
            (-2, 1), (-1, 2), (1, 2), (2, 1),
            (2, -1), (1, -2), (-1, -2), (-2, -1)
        ]

        for dr, dc in directions:
            nr, nc = curr_r + dr, curr_c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == -1:
                if solve(nr, nc, step + 1):
                    return True

        grid[curr_r][curr_c] = -1
        path.pop()
        return False

    if solve(r, c, 1):
        result = []
        for p in path:
            result.append(f"({p[0]},{p[1]})")
        print(" ".join(result))
    else:
        print("Ronda Gagal.")

main()