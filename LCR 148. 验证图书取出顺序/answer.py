class Solution(object):
    def validateBookSequences(self, putIn, takeOut):
        """
        :type putIn: List[int]
        :type takeOut: List[int]
        :rtype: bool
        """
        if len(putIn) == 1:
            return True

        book_list = []
        i = 0
        for book in putIn:
            book_list.append(book)
            while book_list and (book_list[-1] == takeOut[i]):
                book_list.pop()
                i += 1
        
        if len(book_list) > 0:
            return False
        else:
            return True
            
