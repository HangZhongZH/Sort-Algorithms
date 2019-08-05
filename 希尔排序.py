def shellSort(nums):
    length = len(nums)
    gap = 1
    while gap < length // 3:
        gap = gap * 3 + 1 # 动态定义间隔序列
    while gap > 0:
        for i in range(length - gap):
            currentnum = nums[i + gap]
            compareidx = i
            while currentnum < nums[compareidx] and compareidx >= 0:
                nums[compareidx + gap], nums[compareidx] = nums[compareidx], nums[compareidx + gap]
                compareidx -= gap
        gap = gap // 3  # 下一个动态间隔
    return nums