# -*- coding:utf-8 -*-
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # if type(s) is not str:
        #     return

        if s is None or s == "":
            return ''
        else:
            pass

        return s[::-1]


# test
solution = Solution()
print solution.reverseString("hello")
print solution.reverseString('')

