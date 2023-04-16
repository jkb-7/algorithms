def insertionsort(array: list): # sorts ascending
    length = len(array)
    if length < 2: return array
    for i in range(length):
        helper_index = i
        while (helper_index > 0 and array[helper_index] < array[helper_index - 1]):
            array[helper_index], array[helper_index - 1] = array[helper_index - 1], array[helper_index]
            helper_index -= 1
    return array
