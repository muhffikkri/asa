import random

comparisons = 0

def plus_comparison():
    global comparisons
    comparisons += 1

def partition(arr, low, high, pivot_index):
    # Pindahkan pivot yang dipilih ke ujung kanan (high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    
    i = low - 1
    for j in range(low, high):
        plus_comparison()
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high, first_pivot_idx=None):
    if low < high:
        if first_pivot_idx is not None:
            # Gunakan pivot yang ditentukan untuk langkah pertama saja
            p_idx = first_pivot_idx
            first_pivot_idx = None 
        else:
            # Gunakan random pivot untuk rekursi selanjutnya
            p_idx = random.randint(low, high)
        
        pi = partition(arr, low, high, p_idx)
        
        quick_sort(arr, low, pi - 1, first_pivot_idx=None)
        quick_sort(arr, pi + 1, high, first_pivot_idx=None)

def main():
    global comparisons
    # Dataset dengan 8 elemen
    original_data = [23, 52, 32, 34, 21, 12, 49, 29]
    n = len(original_data)
    
    print(sum(original_data)/n)
    print(f"Data Awal: {original_data}")
    print("-" * 50)
    print(f"{'Pivot Awal (Index)':<20} | {'Nilai Pivot':<15} | {'Jumlah Perbandingan'}")
    print("-" * 50)
    
    results = []
    
    for i in range(n):
        test_data = original_data.copy()
        comparisons = 0  # Reset comparisons untuk setiap test
        
        # Jalankan sorting dengan memaksa pivot pertama di index i
        quick_sort(test_data, 0, n - 1, first_pivot_idx=i)
        
        pivot_val = original_data[i]
        results.append((i, pivot_val, comparisons))
        print(f"{i:<20} | {pivot_val:<15} | {comparisons}")

    min_comp = min(row[2] for row in results)
    best_pivots = [row for row in results if row[2] == min_comp]

    print("-" * 50)
    print(f"Comparison paling sedikit: {min_comp}")
    print("Pivot awal paling efisien:")
    for idx, pivot_val, comp in best_pivots:
        print(f"- index {idx} (nilai {pivot_val}) dengan {comp} comparison")

    # Analisis : pivot dekat median cenderung membagi data lebih seimbang
    sorted_data = sorted(original_data)
    median_val = sorted_data[n // 2] if n % 2 == 1 else (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    print("Analisis:")
    print(
        "- Semakin seimbang pembagian kiri/kanan saat partisi awal, "
        "semakin sedikit total comparison yang dibutuhkan."
    )
    print(f"- Median data sekitar: {median_val}")
    print(
        "- Pivot awal dengan nilai yang mendekati median biasanya menghasilkan "
        "kedalaman rekursi lebih kecil, sehingga proses sorting lebih cepat."
    )

    return results

main()