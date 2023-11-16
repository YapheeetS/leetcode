class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.num_list = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.num_list.append(num)
        self.num_list.sort()


    def findMedian(self):
        """
        :rtype: float
        """
        
        if len(self.num_list) % 2 == 0:
            return float(self.num_list[len(self.num_list) // 2 - 1] +  self.num_list[len(self.num_list) // 2]) / 2.0
        else:
            return self.num_list[len(self.num_list) // 2]




# 通过大顶堆和小顶堆实现
from heapq import *

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """

        self.small_heap = [] # 小顶堆，保存较大的一半
        self.big_heap = [] # 大顶堆，保存较小的一半 (实现 大顶堆 方法： 小顶堆的插入和弹出操作均将元素 取反)

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.small_heap) != len(self.big_heap):
            heappush(self.small_heap, num)
            heappush(self.big_heap, -heappop(self.small_heap))
        else:
            heappush(self.big_heap, -num)
            heappush(self.small_heap, -heappop(self.big_heap))

    def findMedian(self):
        """
        :rtype: float
        """
        
        if len(self.small_heap) != len(self.big_heap):
            return self.small_heap[0]
        else:
            return (self.small_heap[0] - self.big_heap[0]) / 2.0





# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()