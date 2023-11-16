class Solution(object):
    def reverseMessage(self, message):
        """
        :type message: str
        :rtype: str
        """
        message = message.strip()
        res = []
        words = []
        print(message)
        for i in range(0, len(message)):
            if i == len(message) - 1:
                words.append(message[i])
                res.append(''.join(words))
            if (i > 0):
                if message[i] == ' ' and message[i-1] == ' ':
                    continue
                if message[i] == ' ':
                    res.append(''.join(words))
                    words = []
                    continue
            words.append(message[i])

        res = res[::-1]
        return ' '.join(res)



class Solution(object):
    def reverseMessage(self, message):
        """
        :type message: str
        :rtype: str
        """
        return ' '.join(message.strip().split()[::-1])
