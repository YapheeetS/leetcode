class Solution(object):
    def pathEncryption(self, path):
        """
        :type path: str
        :rtype: str
        """
        return path.replace('.', ' ')