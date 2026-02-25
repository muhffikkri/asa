def main() :
    x, y, n = list(map(int, input().split()))
    res = []
    j = 0
    i = 0

    while i < n :
        j += 1
        if j % y == 0 : 
            continue
        else :
            res.append(x * j)
            i += 1

    print(" ".join(list(map(str, res))))
    
main()