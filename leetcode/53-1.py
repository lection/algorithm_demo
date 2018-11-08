def max_sub_array_value_o3(nums):
    if not nums or len(nums) == 0:
        return []
    max_value = None
    for start in range(len(nums)):
        for end in range(start + 1, len(nums) + 1):
            sub_arr = nums[start: end]
            sum_value = sum(sub_arr)
            if max_value is None or max_value < sum_value:
                max_value = sum_value
                # max_sub_arr = sub_arr

    return max_value


def max_sub_array_value_o2(nums):
    if not nums or len(nums) == 0:
        return 0
    max_value = None
    for start, num in enumerate(nums):
        sum_value = 0
        for end, new_num in enumerate(nums[start:]):
            sum_value += new_num
            if max_value is None or max_value < sum_value:
                max_value = sum_value

    return max_value


def max_sub_array_value_o1(nums):
    if not nums or len(nums) == 0:
        return 0
    sum_value = 0
    max_value = None
    for num in nums:
        sum_value += num
        if max_value is None:
            max_value = sum_value
            continue
        max_value = max(sum_value, max_value)
        if sum_value < 0:
            sum_value = 0

    return max_value


def max_sub_array_value_o1_2(nums):
    if not nums or len(nums) == 0:
        return 0
    #求数组累加的和
    sum_array = [0]
    sum_value = 0
    for num in nums:
        sum_value += num
        sum_array.append(sum_value)

    max_value = None

    for index, num in enumerate(nums):
        sum_array_min = sum_array[index] if index == 0 else min(sum_array_min, sum_array[index])
        sum_value = sum_array[index + 1]
        if max_value is None:
            max_value = sum_value
        else:
            max_value = max(max_value, sum_value-sum_array_min)
    return max_value


def max_sub_array_value_o1_3(nums):
    if not nums or len(nums) == 0:
        return 0

    max_value = None

    sum_value = 0
    sum_array_min = 0

    for index, num in enumerate(nums):
        sum_array_min = min(sum_array_min, sum_value)
        sum_value += num
        if max_value is None:
            max_value = sum_value
        else:
            max_value = max(max_value, sum_value-sum_array_min)
    return max_value


def test(fn):
    l1 = [1, 2, 3, 4, 5, 6]
    l2 = [0, 2, 5, -1, -2]
    l3 = [1, 2, 1, -2, 3, -5, 2, 1]
    l4 = [-1]
    l5 = [-2, -1]
    print(l1, fn(l1), fn(l1) == sum(l1))
    print(l2, fn(l2), fn(l2) == sum([0, 2, 5]))
    print(l3, fn(l3), fn(l3) == sum([1, 2, 1, -2, 3]))
    print(l4, fn(l4), fn(l4) == -1)
    print(l5, fn(l5), fn(l5) == -1)


print('o3')
test(max_sub_array_value_o3)
print('o2')
test(max_sub_array_value_o2)
print('o1')
test(max_sub_array_value_o1)
print('o1_2')
test(max_sub_array_value_o1_2)
print('o1_3')
test(max_sub_array_value_o1_3)
