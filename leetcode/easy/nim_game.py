# -*- coding:utf-8 -*-
#
# You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you
# take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.
#
# Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.
#
# For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.
#
# Hint:
#
# If there are 5 stones in the heap, could you figure out a way to remove the stones such that you will always be the winner?

# 观察 , 只要是4的倍数个,我们一定会输,所以对4取余即可
# stone result
# 1    Win
# 2    Win
# 3    Win
# 4    Lost ----
# 5    Win
# 6    Win
# 7    Win
# 8    Lost ----
# 9    Win
# 10   Win

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return False if n % 4 == 0 else True


if __name__ == '__main__':
    s = Solution()
    print s.canWinNim(4)
    print s.canWinNim(7)
