def bubbleSort(input_array):
    for j in range(1, len(input_array)):
        print(j, input_array)
        for i in range(1, len(input_array)):
            if input_array[i] < input_array[i - 1]:
                temp = input_array[i]
                input_array[i] = input_array[i - 1]
                input_array[i - 1] = temp
    return input_array

print (bubbleSort([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))
