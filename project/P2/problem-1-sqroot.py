def sqrt(num):
    def _calc_sqrt(num, start, end):
        mid = (start + end) // 2
        delta = num - (mid * mid)
        if delta == 0 or start == end:
            return mid
        if end - start == 1:
            if end ** 2 > num:
                return start
            return end

        # which half should be evaluated next?
        if delta < 0:
            return _calc_sqrt(num, start, mid)
        if delta > 0:
            return _calc_sqrt(num, mid, end)

    # catch edge cases
    if num is None or num < 0:
        print("Unsupported value. Square roots only accepts positive integer")
        return

    if num == 0:
        return 0
    if num == 1:
        return 1

    return _calc_sqrt(num, 0, num // 2)


# TEST
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (sqrt(None) is None) else "Fail")
print("Pass" if (sqrt(-1) is None) else "Fail")
