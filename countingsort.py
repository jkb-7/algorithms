def countingSort(array):
    if len(array) < 2: return array
    helper_array_length = max(array) + 1
    helper_array = [0] * helper_array_length

    # zliczanie poszczególnych elementów
    for i in range(len(array)):
        element = array[i]
        helper_array[element] += 1
    print(helper_array)

    # cumulative_sum of values
    cumulative_sum = 0
    for i in range(helper_array_length):
        helper_array[i] += cumulative_sum
        cumulative_sum = helper_array[i]
    print(helper_array)

    # moving values to the right by 1 space
    helper_array.insert(0,0)
    helper_array = helper_array[:-1]
    print(helper_array)

    output_array = [0] * len(array)
    for i in array:
        index = helper_array[i]
        helper_array[i] += 1
        output_array[index] = i
    print(output_array)
    return output_array

if __name__ == "__main__":
    test_array = [1,7,5,3,14,1,9,7]
    countingSort(test_array)
