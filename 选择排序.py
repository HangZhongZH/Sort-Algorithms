def selectionSort(nums):
    length = len(nums)
    for i in range(length - 1):
        mintempidx = i
        for j in range(i + 1, length):
            if nums[j] < nums[mintempidx]:
                mintempidx = j
        nums[i], nums[mintempidx] = nums[mintempidx], nums[i]
    return nums
print(selectionSort([1,4,2,6,3]))
