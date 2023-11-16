import random

def quick_sort(nums, l, r):
    if l >= r: return
    median = partition(nums, l, r)
    quick_sort(nums, l, median - 1)
    quick_sort(nums, median + 1, r)

# 哨兵划分
def partition(nums, l, r):
    # 在闭区间 [l, r] 随机选取任意索引，并与 nums[l] 交换
    ra = random.randrange(l, r + 1)
    

    i, j = l, r
    while i < j:
        # 需要把j放前面
        while i < j and nums[j] >= nums[l]: j -= 1
        while i < j and nums[i] <= nums[l]: i += 1
        # 此时nums[i] > nums[l] and nums[j] < nums[l]，所以交换nums[i]和nums[j]
        nums[i], nums[j] = nums[j], nums[i]
    # num[l]和nums[i]的交换
    nums[l], nums[i] = nums[i], nums[l]
    return i


# 调用
nums = [3, 4, 1, 5, 0, 2, 22, 12, 4, 6, 18, 2, 1, 9]
quick_sort(nums, 0, len(nums) - 1)
print(nums)



"""
讨论一下为什么partition函数中，对于j和i的搜索顺序不能交换

首先明确一点，在partition的最后一步，我们将nums[ i ]和nums[ l ]交换了位置，即将最左节点放到了数组中间的某个位置，其左边元素比它都小，其右边元素比它都大。显然，最后一步的互换要求nums[ i ]比nums[ l ]更小。
在明确了上面这个条件后，我们就很容易理解为什么在while内部对i和j进行移动操作时，必须先移动j，再移动i。如果我们先移动i的话，那就意味着当i停下来的时候，nums[ i ]指向的可能是比nums[ l ]更大的元素（因为i的循环条件是nums[ i ]<=nums[ l ]），这样我们在执行上面提到的交换操作时，就会造成节点左边存在比它更大元素的情况出现。


"""