# -*- coding:utf-8 -*-

# 374. Guess Number Higher or Lower   QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Contributors: Admin
# We are playing the Guess Game. The game is as follows:
#
# I pick a number from 1 to n. You have to guess which number I picked.
#
# Every time you guess wrong, I'll tell you whether the number is higher or lower.
#
# You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
#
# -1 : My number is lower
#  1 : My number is higher
#  0 : Congrats! You got it!
# Example:
# n = 10, I pick 6.
#
# Return 6.

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
def guess(num):
    """
    :param num:
    :return:
    """
    n = 5
    if num > n:
        return -1
    elif num < n:
        return 1
    else:
        return 0


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not isinstance(n, int):
            return

        start = 1
        end = n
        while start + 1 < end:
            t = (start + end) / 2
            print '-----', t
            res = guess(t)
            if res > 0:
                start = t + 1
            elif res < 0:
                end = t - 1
            else:
                return t
        if guess(start) == 0:
            return start
        if guess(end) == 0:
            return end


if __name__ == '__main__':
    s = Solution()
    print s.guessNumber(10)
