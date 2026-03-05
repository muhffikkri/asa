# Pembuat      : Muhammad Fikri / 24060124130069
# Tanggal      : 1 Maret 2026

def count_chromosome(string, isX, index) -> int:
    if index >= len(string):
        return 0
    
    if string[index] == "X":
        return count_chromosome(string, True, index + 1)
    elif isX and string[index] == "Y":
        return 1 + count_chromosome(string, False, index + 1)
    else :
        return count_chromosome(string, isX, index + 1)
    

def main():
    string = input().strip()
    if not string: 
        print(False)
        return
    totalXY = count_chromosome(string.upper(), False, 0)

    print(totalXY % 2 == 0) 


main()