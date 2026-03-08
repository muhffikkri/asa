# Nama : Muhammad Fikri
# NIM : 24060124130069
# Lab : A2

def fpb(a, b):
    if b == 0:
        return a
    else:
        return fpb(b, a % b)

def apple_weight(n, a, b):
    mod = 1000000007
    
    val = fpb(a, b)
    
    r = b // val
    h = a // val
    k = n // r
    
    apple_distribution = (k * (r + h)) % mod
    
    if val == a:
        return apple_distribution
    else:
        a_new, b_new = val, a
        return (apple_distribution + apple_weight(n, a_new, b_new)) % mod

def main():
    n, a, b = list(map(int, input().split()))
    result = apple_weight(n, a, b)
    print(result)
        
main()