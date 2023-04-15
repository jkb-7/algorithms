def countingSort(array):
    if len(array) < 2: return array
    helper_array_length = max(array) + 1
    helper_array = [0] * helper_array_length

    # counting appearance of each element
    for i in range(len(array)):
        element = array[i]
        helper_array[element] += 1

    # cumulative sum of values
    cumulative_sum = 0
    for i in range(helper_array_length):
        helper_array[i] += cumulative_sum
        cumulative_sum = helper_array[i]

    # moving values to the right by 1 space
    # before that cut out the last element and insert 0 at the beginning
    helper_array.insert(0,0)
    helper_array = helper_array[:-1]

    output_array = [0] * len(array)
    for i in array:
        index = helper_array[i]
        helper_array[i] += 1
        output_array[index] = i
    return output_array
