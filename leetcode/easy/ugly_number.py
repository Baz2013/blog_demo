# -*- coding:utf-8 -*-

# 263. Ugly Number
# Difficulty: Easy
# Write a program to check whether a given number is an ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
#
# Note that 1 is typically treated as an ugly number.

# /** * * 理论： 首先明确几个数学概念和结论
# * 1.奇数必定没有偶数因子;
# * 2.所有质数（除了2）都是奇数;
# * 3.正整数分为质数、合数和1，任一合数必定可以写成若干个质数因子之积（可能会有重复质因子，比如12=2*2*3）;
# * * 从质数2开始，寻找目标整数num的因子（能整除num就是因子），如果当前因子出现多次，
# * 那么都记录下来，且每次都从num中除去该因子，从而每次得到的因子必定是质因子。
# * 因为合数因子本身必定可以写成若干个质数因子之积，而我们是从最小的质数开始寻找， 所以如果能被num整除，则一定是质因子。
# * * 比如num=12，其因子有1、2、3、4、6、12，其中质因子有2和3 由于4=2*2 ，6=2*3，所以当i=4或6时，num%i != 0 * */


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        print num,
        if num < 1:
            return False
        prime_factor = list()
        rst = True
        while 0 == num % 2:
            prime_factor.append(2)
            num /= 2

        i = 3L
        while i < num + 1:
            flag = True
            while 0 == num % i:
                num /= i
                if flag:
                    prime_factor.append(i)
                    flag = False
                else:
                    pass
            if i > 5:
                rst = False
                break
            i += 2

        return rst


if __name__ == '__main__':
    s = Solution()
    print s.isUgly(0)
    print s.isUgly(6)
    print s.isUgly(8)
    print s.isUgly(88888)
    print s.isUgly(7)
    print s.isUgly(14)
    print s.isUgly(16)
    print s.isUgly(27)
    print s.isUgly(30)
    print s.isUgly(214797179)
    print s.isUgly(937351770)
