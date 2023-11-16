class Solution(object):
    def inventoryManagement(self, stock, cnt):
        """
        :type stock: List[int]
        :type cnt: int
        :rtype: List[int]
        """
        # 快速排序
        def partition(stock, l, r):
            i, j = l, r
            while i < j:
                while i < j and stock[j] >= stock[l] : j -= 1
                while i < j and stock[i] <= stock[l]: i += 1
                # 此时 stock[j] <= stock[l] or stock[i] > stock[l] or i == j
                # 因此交换i，j
                stock[i], stock[j] = stock[j], stock[i]
            stock[l], stock[i] = stock[i], stock[l]
            return i

        def quick_sort(stock, l, r):
            if l > r: return
            m = partition(stock, l, r)
            quick_sort(stock, l, m - 1)
            quick_sort(stock, m + 1, r)
        
        quick_sort(stock, 0, len(stock)-1)
        return stock[:cnt]


 # 快速选择
class Solution(object):
    def inventoryManagement(self, stock, cnt):
        """
        :type stock: List[int]
        :type cnt: int
        :rtype: List[int]
        """
        # 快速排序
        def partition(stock, l, r):
            i, j = l, r
            while i < j:
                while i < j and stock[j] >= stock[l] : j -= 1
                while i < j and stock[i] <= stock[l]: i += 1
                # 此时 stock[j] <= stock[l] or stock[i] > stock[l] or i == j
                # 因此交换i，j
                stock[i], stock[j] = stock[j], stock[i]
            stock[l], stock[i] = stock[i], stock[l]
            return i

        def quick_sort(stock, l, r):
            if l > r: return
            m = partition(stock, l, r)
            # 快速选择
            # 增加一个判断，减少递归的次数
            if cnt < m: return quick_sort(stock, l, m - 1)
            if cnt > m: return quick_sort(stock, m + 1, r)
        
        if cnt >= len(stock): return stock
        quick_sort(stock, 0, len(stock)-1)
        return stock[:cnt]
