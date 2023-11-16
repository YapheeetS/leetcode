# 暴力法，超时！
class Solution(object):
    def reversePairs(self, record):
        """
        :type record: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(record)):
            for j in range(i + 1, len(record)):
                if record[i] > record[j]:
                    res += 1
        return res
    

# 归并排序
class Solution(object):
    def reversePairs(self, record):
        """
        :type record: List[int]
        :rtype: int
        合并阶段 本质上是 合并两个排序数组 的过程，而每当遇到 左子数组当前元素 > 右子数组当前元素 时，意味着 「左子数组当前元素 至 末尾元素」 与 「右子数组当前元素」 构成了若干 「逆序对」 。
        """
        def merge_sort(record, l, r):
            if l >= r: return 0
            # 分（划分）
            m = (l + r) // 2
            res = merge_sort(record, l, m) + merge_sort(record, m + 1, r)
            # 治（合并）
            temp = record[l: r + 1]
            i = 0
            j = m - l + 1
            for k in range(l, r + 1):
                if i == m - l + 1:
                    record[k] =  temp[j]
                    j += 1
                elif j == r - l + 1:
                    record[k] = temp[i]
                    i += 1
                elif temp[i] <= temp[j]:
                    record[k] = temp[i]
                    i += 1
                elif temp[i] > temp[j]:
                    record[k] = temp[j]
                    j += 1
                    res += m + 1 - l - i
            return res

        return merge_sort(record, 0, len(record)-1)
        
