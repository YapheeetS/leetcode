class Solution(object):
    def findRepeatDocument(self, documents):
        """
        :type documents: List[int]
        :rtype: int
        """
        for item in dict(Counter(documents)).items():
            if item[1] > 1:
                return item[0]

