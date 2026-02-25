def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def main():
    s = input().strip()
    n = len(s)
    
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
            
    pembilang = factorial(n)
    
    penyebut = 1
    for char in counts:
        penyebut *= factorial(counts[char])
        
    print(pembilang // penyebut)

main()