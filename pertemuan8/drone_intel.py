def main():
    n, m = map(int, input().split())
    
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    
    start_x, start_y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())

    min_cost = -1

    def get_heuristic(cx, cy):
        dx = abs(cx - goal_x)
        dy = abs(cy - goal_y)
        return (1.0 * (dx + dy)) + (1.4 - 2.0) * min(dx, dy)

    open_list = [(get_heuristic(start_x, start_y), 0.0, start_x, start_y)]
    visited_costs = {(start_x, start_y): 0.0}
    
    while open_list:
        best_idx = 0
        for i in range(1, len(open_list)):
            if open_list[i][0] < open_list[best_idx][0]:
                best_idx = i
        
        f, g, x, y = open_list.pop(best_idx)
        
        if x == goal_x and y == goal_y:
            min_cost = g
            break
            
        if g > visited_costs.get((x, y), float('inf')):
            continue
        
        directions = [
            (0, 1, 1.0), (0, -1, 1.0), (1, 0, 1.0), (-1, 0, 1.0),
            (1, 1, 1.4), (1, -1, 1.4), (-1, 1, 1.4), (-1, -1, 1.4)
        ]
        
        for dx, dy, step_cost in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                new_g = g + step_cost
                
                if new_g < visited_costs.get((nx, ny), float('inf')):
                    visited_costs[(nx, ny)] = new_g
                    f_score = new_g + get_heuristic(nx, ny)
                    open_list.append((f_score, new_g, nx, ny))

    if min_cost != -1:
        if min_cost % 1 == 0:
            print(int(min_cost))
        else:
            print(round(min_cost, 1))
    else:
        print("-1")

main()