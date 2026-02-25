def main():
    n = int(input())
    weights = list(map(int, input().split()))

    ganjil = []
    genap = []
    
    for w in weights:
        if w % 2 == 0:
            genap.append(w)
        else:
            ganjil.append(w)
            
    ganjil.sort(reverse=True)
    genap.sort(reverse=True)
    
    max_total = -1

    if len(ganjil) >= 2 and len(genap) >= 1:
        total_a = ganjil[0] + ganjil[1] + genap[0]
        if total_a > max_total:
            max_total = total_a
            
    if len(ganjil) >= 3:
        total_b = ganjil[0] + ganjil[1] + ganjil[2]
        if total_b > max_total:
            max_total = total_b
            
    print(max_total)

main()