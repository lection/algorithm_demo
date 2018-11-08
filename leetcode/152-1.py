import sys

def multiply(nums):
    if nums is None or len(nums) == 0:
        return 0
    result = 1
    for n in nums:
        result *= n
    return result


def test(fn):
    l1 = [1, 2, 3, 4, 5]
    l2 = [2, 3, -2, 4]
    l3 = [-2, 0, -1]
    l4 = [-2, -1, 5, -5]
    l5 = [-10, 1, 5, -2, 2, -3, 6]
    print(l1, fn(l1), fn(l1) == multiply(l1))
    print(l2, fn(l2), fn(l2) == 6)
    print(l3, fn(l3), fn(l3) == 0)
    print(l4, fn(l4), fn(l4) == multiply([-1, 5, -5]))


def max_array_multiply(nums):
    if nums is None or len(nums) == 0:
        return 0

    first_minus = None
    array_multiply = 1
    max_result = nums[0]
    for n in nums:
        if n == 0:
            max_result = max(max_result, 0)
            array_multiply = 1
            first_minus = None
            continue

        array_multiply *= n

        if array_multiply < 0:
            if first_minus is None:
                first_minus = array_multiply
                max_result = max(max_result, array_multiply)
            else:
                max_result = max(max_result, array_multiply/first_minus)
        else:
            max_result = max(max_result, array_multiply)
    return int(max_result)


test(max_array_multiply)