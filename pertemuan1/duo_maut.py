def main():
    n = int(input())
    
    power = list(map(int, input().split()))
    
    max_total = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            total = power[i] + power[j]
            if total > max_total:
                max_total = total
                
    print(max_total)

main()