def merge_sort(nums, l, r):
    if l >= r: return
    m = (l + r) // 2
    merge_sort(nums, l, m)
    merge_sort(nums, m+1, r)
    # 合并
    temp = nums[l: r + 1]
    i = 0
    j = m - l + 1
    for k in range(l, r + 1):
        
        # i超过左边数组的长度
        if i == m - l + 1:
            nums[k] = temp[j]
            j += 1
        # j超过右边数组的长度
        elif j == r - l + 1:
            nums[k] = temp[i]
            i += 1
        
        elif temp[i] <= temp[j]:
            nums[k] = temp[i]
            i += 1
        elif temp[i] > temp[j]:
            nums[k] = temp[j]
            j += 1
        
        


# 调用
nums = [3, 4, 1, 5, 2, 1]
merge_sort(nums, 0, len(nums) - 1)
print(nums)