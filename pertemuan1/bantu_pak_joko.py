def countChr(string: str, char: chr) -> int :
    count = 0
    i = 0
    while i < len(string) :
        if string[i] == char :
            count += 1
        i += 1
    return count

def modus(string: str) -> chr:
    maxCount = 0;
    modusChar = "#"
    i = 0
    while i < len(string) :
        count = countChr(string, string[i])
        if count > maxCount :
            maxCount, modusChar = count, string[i]
        i += 1

    return modusChar

def Joko(string: str) -> list :
    freqChr = modus(string)
    listIndex = []
    i = 0
    while i < len(string) :
        if string[i] != freqChr:
            listIndex.append(str(i + 1))
        i += 1
    return listIndex

def main() :
    string = input()
    res = Joko(string)
    if len(res) == 0 :
        print(-1)
    else :
        print(" ".join(res))

main()