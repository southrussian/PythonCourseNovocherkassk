def include_two_three(array: [float]) -> bool:
    for i in array:
        if i == 2 or i == 3:
            return True
    return False


arr = [2, 5, 7, 8]
arr2 = [7]
print(include_two_three(arr2))
