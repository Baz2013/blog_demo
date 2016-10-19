# -*- coding:utf-8 -*-

# 119. Pascal's Triangle II   QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Contributors: Admin
# Given an index k, return the kth row of the Pascal's triangle.
#
# For example, given k = 3,
# Return [1,3,3,1].
#
# Note:
# Could you optimize your algorithm to use only O(k) extra space?
#
# Subscribe to see which companies asked this question

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1 for x in range(rowIndex + 1)]
        i = 2
        while i <= rowIndex:
            k = i - 1
            while k > 0:
                res[k] = res[k] + res[k - 1]
                k -= 1
            i += 1

        return res


if __name__ == '__main__':
    s = Solution()
    print s.getRow(3)
    print s.getRow(0)
    print s.getRow(1)
    print s.getRow(2)
    print s.getRow(5)
