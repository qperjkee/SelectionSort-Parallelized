def selection_sort(array):
    length = len(array)
    
    for i in range(length - 1):
        min_idx = i
        for j in range(i + 1, length):
            if array[j] < array[min_idx]:
                min_idx = j
                
        if min_idx != i:
            array[i], array[min_idx] = array[min_idx], array[i]

