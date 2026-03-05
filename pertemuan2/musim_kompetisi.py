# Nama : Muhammad Fikri 
# NIM  : 24060124130069
# Lab  : A2

def main():
    line1 = input()
    nOrang = int(line1)
    
    powerList = list(map(int, input().split()))
    
    maxTotal = -float('inf')
    lowPos = 0
    highPos = 0
    
    currentSum = -float('inf')
    startTemp = 0
    
    for i in range(nOrang):
        if currentSum < 0:
            currentSum = powerList[i]
            startTemp = i
        else:
            currentSum += powerList[i]
            
        if currentSum > maxTotal:
            maxTotal = currentSum
            lowPos = startTemp
            highPos = i
        elif currentSum == maxTotal:
            currentSize = i - startTemp + 1
            maxSize = highPos - lowPos + 1
            if currentSize > maxSize:
                lowPos = startTemp
                highPos = i
            elif currentSize == maxSize:
                if startTemp < lowPos:
                    lowPos = startTemp
                    highPos = i
                    
    print(maxTotal)
    print(f"{lowPos + 1} {highPos + 1}")
                
main()