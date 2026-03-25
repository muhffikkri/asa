# Nama : Muhammad Fikri
# NIM : 24060124130069
# Lab : A2

def level(string, n, ordS):
    if n == 1:
        return string
    else :
        return level(string + chr(ordS + 1) + string, n - 1, ordS + 1 if ordS != 90 else 65)

def main():
    n, k = list(map(int, input().split()))
    s = input()
    ordS = ord(s)

    print(level(s, n, ordS)[k - 1])

main()



# Nama : Muhammad Fikri
# NIM : 24060124130069
# Lab : A2

def level(n, k, s_start_ord):
    length_prev = (2 ** (n - 1)) - 1
    mid_pos = length_prev + 1
    
    if n == 1:
        return chr(s_start_ord)
    
    if k < mid_pos:
        return level(n - 1, k, s_start_ord)
    
    elif k == mid_pos:
        char_code = (s_start_ord - ord('A') + (n - 1)) % 26
        return chr(ord('A') + char_code)
    
    else:
        new_k = mid_pos - (k - mid_pos)
        return level(n - 1, new_k, s_start_ord)

def main():
    n, k = list(map(int, input().split()))
    s = input().strip()
    s_start_ord = ord(s)

    print(level(n, k, s_start_ord))
    
main()