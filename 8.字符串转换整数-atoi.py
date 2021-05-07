#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        n, sign, is_pre = 0, 1, True
        for c in s:
            if c == ' ' and is_pre:
                continue
            elif c == '-' and is_pre:
                sign, is_pre = -1, False
            elif c == '+' and is_pre:
                sign, is_pre = 1, False
            elif '0' <= c <= '9':
                n, is_pre = n * 10 + int(c), False
            else:
                break
            if -(1 << 31) > n * sign or n * sign >= (1 << 31):
                break
        return min(max(-(1 << 31), n * sign), (1 << 31) - 1)
# @lc code=end

