# Nama : Muhammad Fikri
# NIM : 24060124130069
# Lab : A2

def swap(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] >= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def searchScore(arr, low, high, k):
    if low <= high:
        pivot_index = swap(arr, low, high)
        
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index > k:
            return searchScore(arr, low, pivot_index - 1, k)
        else:
            return searchScore(arr, pivot_index + 1, high, k)
    return -1

def main():
    n, k = list(map(int, input().split()))
    scores = list(map(int, input().split()))

    target_score = searchScore(scores, 0, n - 1, k - 1)

    count = 0
    for s in scores:
        if s >= target_score:
            count += 1
            
    print(f"{target_score} {count}")

main()