def min_element_index(array: list, beginning):
    min_index = beginning
    min_number = array[beginning]
    for i in range(beginning, len(array)):
        if array[i] < min_number:
            min_number = array[i]
            min_index = i
    return min_index

def selectionsort(array: list): # ascending order
    for i in range(len(array) - 1):
        min_index = min_element_index(array, i)
        if i != min_index:
            array[i], array[min_index] = array[min_index], array[i]
    return array
