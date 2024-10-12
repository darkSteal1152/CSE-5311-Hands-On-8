def quicksort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, q + 1, r)


def partition(arr, p, r):
    pivot_index = r
    pivot = arr[pivot_index]

    i = p - 1
    for j in range(p, r):
        if arr[j] <= pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    temp = arr[i + 1]
    arr[i + 1] = arr[r]
    arr[r] = temp

    return i + 1

def order_stat(arr, i):
    p = 0
    r = len(arr) - 1
    while p <= r:
        q = partition(arr, p, r)
        if q == i:
            return arr[q]
        elif q < i:
            p = q + 1
        else:
            r = q - 1
    return None

arr = [15, 6, 9, 8, 4, 17, 3, 5]
for i in range(1, len(arr) + 1):
    result = order_stat(arr, i - 1)
    print(f"The {i}-th smallest element is: {result}")
