def countSort(input_array):
    """
    this function implement the countsort sorting algo and return a sorted array

    """
    max_element = max(input_array)
    initial_array = [0] * (max_element + 1)
    for element in range(0, len(input_array)):
        initial_array[input_array[element]] += 1

    index = 0
    for i in range(0, len(initial_array)):
        while initial_array[i] > 0:
            input_array[index] = i
            index += 1
            initial_array[i] -= 1

    return input_array


if __name__ == '__main__':
    input_array = list(map(int, input("Enter the elements to be sorted! : \t\n").split()))
    print("Array Before Sorting :\n \t")
    print(input_array)
    countSort(input_array)
    print("Array After Sorting :\n \t")
    print(input_array)
