# Pembuat      : Muhammad Fikri / 24060124130069
# Tanggal      : 1 Maret 2026

def buildSurgeSieve(maxLimit):
    surge = [True] * (maxLimit + 1)
    surge[0] = False
    
    if maxLimit >= 2:
        for p in range(2, int(maxLimit**0.5) + 1):
            if surge[p]:
                for i in range(p * p, maxLimit + 1, p):
                    surge[i] = False
    return surge

def main():
    input_q = input()
    qAttempt = int(input_q)
    
    rangeList = []
    maxUpper = 0
    for _ in range(qAttempt):
        rangeI = list(map(int, input().split()))
        rangeList.append(rangeI)
        if rangeI[1] > maxUpper:
            maxUpper = rangeI[1]
    
    isSurge = buildSurgeSieve(maxUpper)
    
    prefixSum = [0] * (maxUpper + 1)
    for i in range(1, maxUpper + 1):
        prefixSum[i] = prefixSum[i-1] + (1 if isSurge[i] else 0)
        
    for i in range(qAttempt):
        lower, upper = rangeList[i]
        
        totalNum = prefixSum[upper] - prefixSum[lower - 1]
        print(totalNum)
        
        if qAttempt == 1:
            surgeNumList = []
            for num in range(lower, upper + 1):
                if isSurge[num]:
                    surgeNumList.append(num)
            print(" ".join(map(str, surgeNumList)))
main()