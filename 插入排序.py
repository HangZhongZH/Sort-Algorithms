def insertionSort(nums):
    length = len(nums)
    for i in range(length - 1):
        idx = i
        currentnum = nums[i + 1]
        while currentnum < nums[idx] and idx >= 0:
            nums[idx + 1], nums[idx] = nums[idx], nums[idx + 1]
            idx -= 1
    return nums
