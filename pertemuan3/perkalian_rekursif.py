# Nama : Muhammad Fikri
# NIM : 24060124130069
# Lab : A2

def kali(a, b):
    if b == 0: 
        return 0
    elif b == 1:
        return a
    else : 
        temp = kali(a, b // 2)
        if b % 2 == 0:
            return temp + temp
        else:
            return a + temp + temp

def main():
    a, b = list(map(int, input().split()))
    if a > b : 
        print(kali(a, b))
    else :
        print(kali(b, a))

main()