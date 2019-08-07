# 空间复杂度为O(NlogN)
def quickSort(nums):
    if len(nums) <= 1:
        return nums
    else:
        less = []
        equal = []
        more = []
        pivot = nums[0]
        for item in nums:
            if item < pivot:
                less.append(item)
            elif item > pivot:
                more.append(item)
            else:
                equal.append(item)
        return quickSort(less) + equal + quickSort(more)

print(quickSort([1,5,2,7,3,9,4,0,4]))



# 空间复杂度为O(logN)
def quickSort2(nums, l, r):
    # 分区操作
    if l < r:
        pivotidx = partition(nums, l, r)
        quickSort2(nums, l, pivotidx - 1)
        quickSort2(nums, pivotidx + 1, r)
    return nums

def partition(nums, l, r):
    pivot = nums[l]
    while l < r:
        while l < r and nums[r] > pivot:
            r -= 1
        nums[r], nums[l] = nums[l], nums[r]
        while l < r and nums[l] <= pivot:
            l += 1
        nums[l], nums[r] = nums[r], nums[l]
    return l


print(quickSort2([1,5,2,7,3,9,4,0,4], 0, 8))
