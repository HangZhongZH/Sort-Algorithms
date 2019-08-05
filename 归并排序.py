def mergeSort(nums):
# 合并
    def merge(lnums, rnums):
        l, r = 0, 0
        res = []
        while l <= len(lnums) - 1 and r <= len(rnums) - 1:
            if lnums[l] < rnums[r]:
                res.append(lnums[l])
                l += 1
            else:
                res.append(rnums[r])
                r += 1
        res = res + lnums[l: ] + rnums[r: ]
        return res
    # 拆分（递归）
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    lnums = mergeSort(nums[: mid])
    rnums = mergeSort((nums[mid: ]))
    return merge(lnums, rnums)


if __name__ == '__main__':
    print(mergeSort([1, 2, 3, 2, 6, 3, 5, 78, 4, 0, 5]))
