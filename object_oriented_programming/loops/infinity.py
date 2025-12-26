def find_max(nums):
    max_so_far = float("-inf")
    if nums == []:
        negative_infinity = float("-inf")
        return negative_infinity
    max = nums[0]
    for x in nums:
        if x > max:
            max = x

    return max
    pass
