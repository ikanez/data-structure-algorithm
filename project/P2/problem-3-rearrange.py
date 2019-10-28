def sort_a_little_bit(items, begin_index, end_index):
    left_index = begin_index
    pivot_index = end_index
    pivot_value = items[pivot_index]

    while pivot_index != left_index:

        item = items[left_index]

        if item <= pivot_value:
            left_index += 1
            continue

        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = pivot_value
        items[pivot_index] = item
        pivot_index -= 1

    return pivot_index


def sort_all(items, begin_index, end_index):
    if end_index <= begin_index:
        return

    pivot_index = sort_a_little_bit(items, begin_index, end_index)
    sort_all(items, begin_index, pivot_index - 1)
    sort_all(items, pivot_index + 1, end_index)


def quicksort(items):
    sort_all(items, 0, len(items) - 1)


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    quicksort(input_list)

    sum1 = 0
    sum2 = 0
    i = 0
    factor = 1

    while i < len(input_list):
        sum1 += input_list[i] * factor
        if i + 1 < len(input_list):
            sum2 += input_list[i + 1] * factor
        factor *= 10
        i += 2

    return sum1, sum2


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# normal
test_case = [[1, 2, 3, 4, 5], [542, 31]]
test_function(test_case)
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

# edge cases
test_case = [[], []]
test_function(test_case)
test_case = [[1], [1]]
test_function(test_case)
test_case = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [86420, 97531]]
test_function(test_case)
