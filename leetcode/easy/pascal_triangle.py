# -*- coding:utf-8 -*-

# 118. Pascal's Triangle   QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Contributors: Admin
# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        if numRows == 0:
            return res
        elif numRows == 1:
            res.append([1])
            return res
        else:
            res.append([1])
            res.append([1, 1])
        i = 2
        while i < numRows:
            tmp = list()
            tmp.append(1)
            pre_lst = res[i - 1]
            for n in range(len(pre_lst)):
                if n + 1 <= len(pre_lst) - 1:
                    tmp.append(pre_lst[n] + pre_lst[n + 1])
                else:
                    tmp.append(1)
            res.append(tmp)
            i += 1

        return res


if __name__ == '__main__':
    s = Solution()
    print s.generate(5)
    print s.generate(2)
    print s.generate(1)
    print s.generate(0)
