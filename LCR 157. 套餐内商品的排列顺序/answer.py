class Solution(object):
    def goodsOrder(self, goods):
        """
        :type goods: str
        :rtype: List[str]
        """
        if goods == '': return []
        res = []
        goods = list(goods)
        used = [0] * len(goods)
        def dfs(goods, used, path):
            if len(path) == len(goods):
                res.append(''.join(path)) 
                return
            for i in range(len(goods)):
                if not used[i]:
                    if i > 0 and goods[i] == goods[i-1] and not used[i-1]:
                        continue
                    used[i] = 1
                    path.append(goods[i])
                    dfs(goods, used, path)
                    path.pop()
                    used[i] = 0
            
        dfs(sorted(goods), used, [])
        return res
    
