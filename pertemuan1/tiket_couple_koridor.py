def main():
    line1 = input().split()
    n = int(line1[0])
    
    line2 = input().split()
    t = int(line2[0])
    
    tiket = list(map(int, input().split()))

    res = -1
    dilihat = {}

    for angka in tiket:
        pasangan = t - angka
        
        if pasangan in dilihat:
            produk_saat_ini = angka * pasangan
            if produk_saat_ini > res:
                res = produk_saat_ini
        
        dilihat[angka] = True

    print(res)

main()