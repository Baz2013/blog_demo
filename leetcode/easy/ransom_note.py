# -*- coding:utf-8 -*-
#
# Given  an  arbitrary  ransom  note  string  and  another  string  containing  letters from  all  the  magazines,  write  a  function  that  will  return  true  if  the  ransom   note  can  be  constructed  from  the  magazines ;  otherwise,  it  will  return  false.   
#
# Each  letter  in  the  magazine  string  can  only  be  used  once  in  your  ransom  note.
#
# Note:
# You may assume that both strings contain only lowercase letters.
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

# 要正确理解题目,找的是"letter" 不是 "word"

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        lst_ran = list(ransomNote)
        lst_mag = list(magazine)
        for c in lst_ran:
            if c in lst_mag:
                lst_mag.pop(lst_mag.index(c))
            else:
                return False

        return True

if __name__ == '__main__':
    s = Solution()
    print s.canConstruct('a', 'b')
    print s.canConstruct('aa', 'ab')
    print s.canConstruct('aa', 'aab')
    print s.canConstruct("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj")
    print s.canConstruct("fffbfg", "effjfggbffjdgbjjhhdegh")
