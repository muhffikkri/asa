def main() :
    D, M = list(map(int, input().split()))
    DNum = list(map(int, input().split()))
    MNum = list(map(int, input().split()))

    res = []

    for i in range(D) :
        for j in range(M) :
            if DNum[i] == MNum[j] : break
        else :
            res.append(DNum[i])

    if len(res) == 0 : 
        print("KOSONG")
    else : 
        print(" ".join(list(map(str, res))))

main()