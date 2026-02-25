def manual_bisect_left(arr, x):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def manual_bisect_right(arr, x):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < arr[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo

def solve():
    line1 = input().split()
    n = int(line1[0])
    q = int(line1[1])
    
    a = list(map(int, input().split()))

    pos_map = {}
    for i in range(n):
        val = a[i]
        if val not in pos_map:
            pos_map[val] = []
        pos_map[val].append(i + 1) 
    
    for _ in range(q):
        query = input().split()
        l = int(query[0])
        r = int(query[1])
        
        range_len = r - l + 1
        found = False
        
        samples = []
        for i in range(l-1, r):
            samples.append(a[i])
        
        checked = {}
        
        for candidate in samples:
            if candidate in checked:
                continue
            checked[candidate] = True
            
            indices = pos_map[candidate]
            count = manual_bisect_right(indices, r) - manual_bisect_left(indices, l)
            
            if count > range_len // 2:
                print(candidate)
                found = True
                break
        
        if not found:
            print("-1")

solve()