def binary_search(input_array, value):
    beg = 0;
    end = len(input_array) - 1;
    
    for i in input_array:
        mid = (end + beg) / 2;
        if i > value:
            beg = mid + 1;
        elif i < value:
            end = mid - 1;
        else:
            return input_array.index(i)
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
