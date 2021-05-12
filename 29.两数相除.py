#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_neg = (dividend < 0 and divisor > 0) or (
            dividend > 0 and divisor < 0)
        if dividend <= -(1 << 31) and divisor == -1:
            return (1 << 31) - 1
        dividend, divisor = abs(dividend), abs(divisor)
        n = 32
        ans = 0
        while dividend >= 0 and n > 0:
            while (dividend - (divisor << n)) < 0 and n > 0:
                n -= 1
            if (dividend - (divisor << n)) < 0:
                break
            dividend -= (divisor << n)
            ans += (1 << n)
        return -ans if is_neg else ans
# @lc code=end
