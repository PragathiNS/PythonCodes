def binarySearch(input_array, element):
    beg = 0
    end = len(input_array) - 1
    for i in input_array:
        mid = end + beg / 2
        if i > element:
            beg = mid + 1
        elif i < element:
            end = mid - 1
        else:
            return input_array.index(i)
    return -1

test1 = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print (binarySearch(test1, test_val1))
print (binarySearch(test1, test_val2))
