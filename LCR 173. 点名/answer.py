class Solution(object):
    def takeAttendance(self, records):
        """
        :type records: List[int]
        :rtype: int
        """

        for i, num in enumerate(records):
            if i != num:
                return i
        return len(records)