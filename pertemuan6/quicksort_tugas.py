import random

def partition(arr, low, high, pivot_index):
    # Pindahkan pivot yang dipilih ke ujung kanan (high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        p_idx = random.randint(low, high)
        pi = partition(arr, low, high, p_idx)
        
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def main():
    # Dataset dengan 8 elemen
    original_data = [4, 2, 9, 8, 0, 3, 1]
    n = len(original_data)
    print(original_data)
    
    results = []
    
    quick_sort(original_data, 0, n - 1)
    
    print(original_data)
    return results

main()