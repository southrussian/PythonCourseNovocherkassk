def new_lists(array: [int]):
    appended_array = []
    for i in array:
        arr = [*range(0, i+1, 1)]
        appended_array.append(arr)
        # array.append(arr)
    return appended_array


arr1 = [6, 8, 3]
print(new_lists(arr1))
