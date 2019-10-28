def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    first_idx = 0
    last_idx = len(input_list) - 1
    idx = -1
    while (first_idx <= last_idx) and (idx == -1):
        mid_idx = (first_idx + last_idx) // 2
        if input_list[mid_idx] == number:
            idx = mid_idx
        else:
            if (
                number < input_list[mid_idx] and number >= input_list[first_idx]
            ):  # if value is smaller then mid index
                last_idx = mid_idx - 1
            elif (
                number >= input_list[first_idx]
                and number > input_list[mid_idx]
                and number > input_list[last_idx]
            ):  # means pivot on the left side
                last_idx = mid_idx - 1
            else:
                first_idx = mid_idx + 1

    return idx


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# normal cases
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# edge cases
test_function([[], None])
test_function([[1], 0])
