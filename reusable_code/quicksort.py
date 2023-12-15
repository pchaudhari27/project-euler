def partition(unsorted_list, low, high):
    # choose rightmost element as pivot
    pivot = unsorted_list[high]
    # start i as pointing to left of list
    i = low - 1

    for j in range(low, high):
        # if element is < pivot
        if unsorted_list[j] <= pivot:
            # swap element with pointer on left of list
            i += 1
            unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]
    
    unsorted_list[i + 1], unsorted_list[high] = unsorted_list[high], unsorted_list[i + 1]
    
    return i + 1
        

def quicksort(unsorted_list, low, high):
    if low < high:
        pivot = partition(unsorted_list, low, high)

        quicksort(unsorted_list, low, pivot - 1)
        quicksort(unsorted_list, pivot, high)
    
    return unsorted_list