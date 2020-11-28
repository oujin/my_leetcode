#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        s, e, m = 1, n, (1+n) // 2
        while s < m < e:
            res = guess(m)
            if res < 0:
                m, e = (s+m)//2, m
            elif res > 0:
                s, m = m, (m+e)//2
            else:
                return m
        if guess(e) == 0:
            return e
        return s
        

        
# @lc code=end

