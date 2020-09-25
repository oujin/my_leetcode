#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)[::-1]
        if x < 0:
            s = s[-1] + s[:-1]
        y = int(s)
        if -(2 ** 31) <= y < 2 ** 31 - 1:
            return y
        return 0
    
    # def reverse(self, x):
    #     x, y, s = abs(x), 0, int(x < 1)
    #     while x:
    #         x, y = x // 10, y * 10 + x % 10
    #     y *= (-1) ** s
    #     return y if -2**31 <= y < 2**31-1 else 0


# @lc code=end

