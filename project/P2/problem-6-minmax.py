def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None

    if len(ints) == 1:
        return (ints[0], ints[0])

    min_v = 0
    max_v = 0

    for i in ints:
        if i < min_v:
            min_v = i
        elif i > max_v:
            max_v = i

    return (min_v, max_v)


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# edge cases
print("Pass" if ((1, 1) == get_min_max([1])) else "Fail")
# print("Pass" if ((None, None) == get_min_max([None])) else "Fail")
print("Pass" if ((0, 4) == get_min_max([4, 1, 2, 3, 1, 1, 2, 0])) else "Fail")
print("Pass" if ((-3, 4) == get_min_max([4, 1, 2, -3, 1, 1, 2, 0])) else "Fail")
