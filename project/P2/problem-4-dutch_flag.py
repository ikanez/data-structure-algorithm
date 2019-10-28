def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    idx_2 = len(input_list) - 1
    idx_0 = 0
    idx_curr = 0

    while idx_curr <= idx_2:
        val_curr = input_list[idx_curr]
        if val_curr == 0:  # idx_0 is only updated when val_curr = 0
            input_list[idx_curr] = input_list[idx_0]
            input_list[idx_0] = val_curr
            idx_0 += 1
            idx_curr += 1
        elif val_curr == 1:
            idx_curr += 1
        elif val_curr == 2:  # idx_2 is only updated when val_curr = 2
            input_list[idx_curr] = input_list[idx_2]
            input_list[idx_2] = val_curr
            idx_2 -= 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function(
    [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
)
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([1, 1, 1, 0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])

# edge cases - the question have determined that possible values can only be within 0,1,2.
test_function([2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])  # reverse order
test_function([])  # empty
test_function([1, 2, 0])  # short list

