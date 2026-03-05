# Nama : Muhammad Fikri 
# NIM  : 24060124130069
# Lab  : A2

def nCr_mod(n, r, mod):
    if r < 0 or r > n:
        return 0
    if r == 0 or r == n:
        return 1
    if r > n // 2:
        r = n - r
    
    num = 1
    for i in range(r):
        num = (num * (n - i)) % mod
    
    den = 1
    for i in range(1, r + 1):
        den = (den * i) % mod
    
    return (num * pow(den, mod - 2, mod)) % mod

def main():
    MOD = 10**9 + 7
    
    line1 = input().split()
    n = int(line1[0])
    k = int(line1[1])
    a = list(map(int, input().split()))
    
    total_sum = sum(a)
    
    if total_sum % k != 0:
        print(0)
        return
    
    s_avg = total_sum // k
    
    if s_avg == 0:
        m = 0
        current_prefix = 0
        for i in range(n - 1):
            current_prefix += a[i]
            if current_prefix == 0:
                m += 1
        
        print(nCr_mod(m, k - 1, MOD))
        
    else:
        ways = [0] * k
        ways[0] = 1 
        
        current_prefix = 0
        for i in range(n - 1):
            current_prefix += a[i]
            
            if current_prefix % s_avg == 0:
                j = current_prefix // s_avg
                if 1 <= j < k:
                    ways[j] = (ways[j] + ways[j-1]) % MOD
        
        print(ways[k-1])

main()