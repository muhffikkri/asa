def main():
    n = int(input())
    
    communication_path = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        communication_path[u].append(v)
        communication_path[v].append(u)
    
    report_path = []
    while len(report_path) < n:
        report_path.extend(map(int, input().split()))
    
    if report_path[0] != 1:
        print("Tidak")
        return

    pos_index = [0] * (n + 1)
    for i in range(n):
        pos_index[report_path[i]] = i
        
    for i in range(1, n + 1):
        communication_path[i].sort(key=lambda x: pos_index[x])
        
    result_path = []
    queue = [1]
    visited = [False] * (n + 1)
    visited[1] = True
    
    current_pos = 0 
    
    while current_pos < len(queue):
        u = queue[current_pos]
        current_pos += 1
        result_path.append(u)
        
        for neighbor in communication_path[u]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                
    if result_path == report_path:
        print("Ya")
    else:
        print("Tidak")

main()