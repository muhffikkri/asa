# Nama : Muhammad Fikri 
# NIM  : 24060124130069
# Lab  : A2

def main():
    input_awal = input().split()
    n_mobil = int(input_awal[0])
    min_kapasitas = int(input_awal[1])
    min_kenyamanan = int(input_awal[2])

    list_mobil = []
    for _ in range(n_mobil):
        p, v, c = list(map(int, input().split()))
        list_mobil.append((p, v, c))

    min_total_biaya = 21000000 

    for i in range(1 << n_mobil):
        current_kapasitas = 0
        current_kenyamanan = 0
        current_biaya = 0
        
        for j in range(n_mobil):
            if (i >> j) & 1:
                current_kapasitas += list_mobil[j][0]
                current_kenyamanan += list_mobil[j][1]
                current_biaya += list_mobil[j][2]
        
        if current_kapasitas >= min_kapasitas and current_kenyamanan >= min_kenyamanan:
            if current_biaya < min_total_biaya:
                min_total_biaya = current_biaya

    print(min_total_biaya)

main()