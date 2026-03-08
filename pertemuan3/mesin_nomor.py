# Nama : Muhammad Fikri
# NIM : 24060124130069
# Lab : A2

def subStr(val):
    if len(val) == 1:
        return val
    else :
        count = 0
        for i in val:
            count += int(i)
        else :
            return subStr((str(count)))

def main():
    n = list(map(int, input().split()))
    k = input()

    p = list(map(lambda x: x * k, n))
    res = subStr("".join(list(map(str, p))))

    print(int(res))
    if int(res) % 2 == 0:
        print("A")
    else :
        print("B")

main()