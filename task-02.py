def find_by_quick_select(array, k):
    if k < 1:
        raise Exception("Invalid position of element") 
    if len(array) < k:
        raise Exception("List has less element than k") 

    pivot = array[0]

    less = [el for el in array if el < pivot]
    more = [el for el in array if el > pivot]
    # print(pivot, less, more)

    if len(less) + 1 == k:
        element = pivot
    elif len(less) >= k:
        element = find_by_quick_select(less, k) 
    elif len(less) + 1 < k:
        k = k - (len(less) + 1)
        element = find_by_quick_select(more, k)

    return element

arr = [38, 27, -30, -20, 9, -40, 82, 10, -10, 16, 101]
# arr = [30]
element = find_by_quick_select(arr, 3)
print(element)
