
# dfs
class Solution(object):
    def wardrobeFinishing(self, m, n, cnt):
        """
        :type m: int
        :type n: int
        :type cnt: int
        :rtype: int
        """
        def dfs(i, j, si, sj):
            if i >= m or j >= n or cnt < si + sj or (i, j) in visited: return 0
            visited.add((i,j))
            if (i + 1) % 10:
                x = si + 1
            else:
                x = si - 8
            if (j + 1) % 10:
                y = sj + 1
            else:
                y = sj - 8
            # 返回 1 + 右方搜索的可达解总数 + 下方搜索的可达解总数，代表从本单元格递归搜索的可达解总数。
            return 1 + dfs(i + 1, j, x, sj) + dfs(i, j + 1, si, y)
            
        visited = set()
        return dfs(0, 0, 0, 0)


# BFS
class Solution(object):
    def wardrobeFinishing(self, m, n, cnt):
        """
        :type m: int
        :type n: int
        :type cnt: int
        :rtype: int
        """
        i = j = 0
        visited = set()
        deque = collections.deque()
        deque.append((i, j))
        res = 0
        while deque:
            i, j = deque.popleft()
            if (i, j) in visited: continue
            visited.add((i, j))
            # 计算当前格子是否符合要求
            num_i, num_j = i, j
            si = sj = 0
            while num_i != 0:
                si += num_i % 10
                num_i = num_i // 10
            while num_j != 0:
                sj += num_j % 10
                num_j = num_j // 10
            if si + sj > cnt: continue
            if i + 1 < m: deque.append((i+1, j))
            if j + 1 < n: deque.append((i, j+1))
            res += 1
        return res




