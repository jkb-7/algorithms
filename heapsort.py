def heapify(array: list, i: int):
    length = len(array)
    left = 2*i + 1
    right = 2*i + 2

    if left <= length - 1 and array[left] > array[i]:
        max = left
    else: max = i

    if right <= length - 1 and array[right] > array[max]:
        max = right

    if max != i:
        array[i], array[max] = array[max], array[i]
        heapify(array, max)
    return array


def build_heap(array):
    length = len(array)
    for i in range(int(length/2) - 1, -1, -1):
        heapify(array, i)
    return array


def heap_sort(array):
    if len(array) < 2: return array
    build_heap(array)
    sorted_array = []

    for i in range(len(array)):
        array[0], array[-1] = array[-1], array[0]
        sorted_array.insert(0, array.pop(-1))
        heapify(array, 0)
    return array

