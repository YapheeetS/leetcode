class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        col_dict = {}
        for word in words:
            for i, ch in enumerate(word):
                if i in col_dict:
                    col_dict[i] += ch
                else:
                    col_dict[i] = ch
        
        for i, word in enumerate(words):
            if word != col_dict[i]:
                return False
        return True
                

# 使用zip(*)实现
class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        max_len = max([len(word) for word in words])
        words = [word + (max_len - len(word))*"$" for word in words]
        # zip 打包为元组的列表, zip(*)则是能将二维数组按每一列展开
        temp = zip(*words)
        print(temp)
        col_words = ["".join(item) for item in temp]
        return col_words == words
