class Solution(object):
    def countTarget(self, scores, target):
        """
        :type scores: List[int]
        :type target: int
        :rtype: int
        """
        return Counter(scores)[target]
    

# 二分查找
class Solution(object):
    def countTarget(self, scores, target):
        """
        :type scores: List[int]
        :type target: int
        :rtype: int
        """
        def binary_search(scores, target):
            l = 0
            r = len(scores)
            while l < r:
                mid = (l + r) // 2
                if scores[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            return l
        
        return binary_search(scores, target + 1) - binary_search(scores, target)