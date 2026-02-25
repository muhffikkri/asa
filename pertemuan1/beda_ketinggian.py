def main():
    n = int(input())
    listOfHeight = list(map(int, input().split()))

    cleaned = []
    if n > 0:
        cleaned.append(listOfHeight[0])
        for i in range(1, n):
            if listOfHeight[i] != listOfHeight[i-1]:
                cleaned.append(listOfHeight[i])
    
    if len(cleaned) < 2:
        print(0)
        return

    extrema = []
    extrema.append(cleaned[0]) 
    
    for i in range(1, len(cleaned) - 1):
        if cleaned[i] > cleaned[i-1] and cleaned[i] > cleaned[i+1]:
            extrema.append(cleaned[i])
        elif cleaned[i] < cleaned[i-1] and cleaned[i] < cleaned[i+1]:
            extrema.append(cleaned[i])
            
    extrema.append(cleaned[-1])

    max_diff = 0
    for i in range(1, len(extrema)):
        diff = abs(extrema[i] - extrema[i-1])
        if diff > max_diff:
            max_diff = diff
            
    print(max_diff)  

    
main()