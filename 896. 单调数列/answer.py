class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        flag_increase = True

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i] < nums[i+1]:
                flag_increase = True
                break
            if nums[i] > nums[i+1]:
                flag_increase = False
                break
        
        for i in range(len(nums) - 1):
            if flag_increase == True:
                if nums[i] > nums[i+1]:
                    return False
            else:
                if nums[i] < nums[i+1]:
                    return False

        return True