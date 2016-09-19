# -*- coding:utf-8 -*-

# 401. Binary Watch  QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom
# represent the minutes (0-59).
#
# Each LED represents a zero or one, with the least significant bit on the right.
#
# For example, the above binary watch reads "3:25".
#
# Given a non-negative integer n which represents the number of LEDs that are currently on,
# return all possible times the watch could represe
#
# Example:
# Input: n = 1
# Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
#
# Note:
# The order of output does not matter.
# The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
# The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid,
#   it should be "10:02".

import itertools


class Solution(object):
    def get_group(self, r_num):
        """
        :param r_num:
        :return:
        """
        lst = list()
        for i in range(0, 5):
            for j in range(0, 7):
                if i + j == r_num:
                    lst.append((i, j))

        return lst

    def get_binary_time(self, r_hour, r_min):
        """
        :param r_item:
        :return:
        """
        rst_lst = list()
        binary_hour_lst = self.get_binary_str(r_hour, 4)
        # print binary_hour_lst
        binary_min_lst = self.get_binary_str(r_min, 6)
        # print binary_min_lst

        for h in binary_hour_lst:
            for m in binary_min_lst:
                rst_lst.append((h, m))
        # print rst_lst
        return rst_lst

    def get_binary_str(self, r_hour, r_max_num):
        """

        :param r_hour:
        :return:
        """
        rst_lst = list()
        h_lst = list()
        b_h_lst = list()
        for i in range(r_hour):
            h_lst.append(1)
        for i in range(r_max_num - r_hour):
            h_lst.append(0)
        gen_rst = itertools.permutations(h_lst)
        for i in gen_rst:
            # print ''.join([str(j) for j in i])
            b_h_lst.append(''.join([str(j) for j in i]))
        # print h_lst
        b_h_lst = list(set(b_h_lst))

        return b_h_lst

    def get_real_time(self, r_item):
        """
        :param r_item:
        :return:
        """
        hour = int(r_item[0], 2)
        min = int(r_item[1], 2)
        if hour > 11 or min > 59:
            # print "#########################%d:%02d" % (hour, min)
            tmp_time = None
        else:
            tmp_time = "%d:%02d" % (hour, min)

        return tmp_time

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        rst_lst = list()
        possible_group = self.get_group(num)
        # print possible_group
        possible_binary_group = list()
        for item in possible_group:
            tmp = self.get_binary_time(item[0], item[1])
            possible_binary_group += tmp

        for i in possible_binary_group:
            real_time = self.get_real_time(i)
            if real_time is not None:
                rst_lst.append(real_time)

        print rst_lst

        return rst_lst


if __name__ == '__main__':
    s = Solution()
    s.readBinaryWatch(1)
    s.readBinaryWatch(2)
    s.readBinaryWatch(3)
    s.readBinaryWatch(4)
    s.readBinaryWatch(5)
    s.readBinaryWatch(6)
    s.readBinaryWatch(7)
    s.readBinaryWatch(8)
