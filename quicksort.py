import random

def quicksort(array):
    if len(array) < 2: return array
    
    rand_index = random.randint(0, len(array) - 1)
    pivot = array.pop(rand_index)

    left = [i for i in array if i <= pivot]
    right = [i for i in array if i > pivot]
    
    return quicksort(left) + [pivot] + quicksort(right)

test_array = [2,89,11,123,1782676,0.5]
print(quicksort(test_array))
