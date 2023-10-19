# 超大数组
class MyHashMap(object):

    def __init__(self):
        self.dict_list = [-1]*(10**6+1)


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.dict_list[key] = value


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        return self.dict_list[key]


    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.dict_list[key] = -1



# 不定长拉链数组
class MyHashMap(object):

    def __init__(self):
        # 分桶数一般取质数，这是因为经验上来说，质数个的分桶能让数据更加分散到各个桶中
        # 1009 是大于 1000 的第一个质数。
        self.buckets = 1009
        self.table = [[] for _ in range(self.buckets)]


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        hashkey = key % self.buckets
        for item in self.table[hashkey]:
            if item[0] == key:
                item[1] == value
                return
        self.table[hashkey].append([key,value])


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        hashkey = key % self.buckets
        for item in self.table[hashkey]:
            if item[0] == key:
                return item[1]


    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hashkey = key % self.buckets
        for i, item in enumerate(self.table[hashkey]):
            if item[0] == key:
                self.table[hashkey].pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

