# 通过，但时间复杂度太高
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] == 0 and nums[j] != 0:
                    nums[i] = nums[j]
                    nums[j] = 0


# 双指针, 两次循环
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        # 双指针
        i = j = 0
        while(i < len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            i += 1
        
        for index in range(j, len(nums)):
            nums[index] = 0


# 双指针一次循环
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        # 用指针j记录需要把非0数组换到的位置
        j = 0
        # i和j首先会同时走到数组中第一个0的元素的位置，然后开始交换操作
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        

