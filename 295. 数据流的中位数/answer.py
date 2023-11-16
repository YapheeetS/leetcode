from heapq import heappush, heappop

class MedianFinder(object):

    def __init__(self):

        self.small_heap = []
        self.big_heap = []


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