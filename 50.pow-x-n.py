#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1 / x, -n)
        if n == 0:
            return 1
        if x == 0 or x == 1:
            return x
        if x == -1:
            return -1 if n % 2 else 1
        ans, n, y, flag = abs(x), n - 1, abs(x), int(x < 0 and n % 2)
        while n > 0:
            if n % 2:
                ans *= y
            y = y ** 2
            if -1e-8 <= ans - y * ans <= 1e-8:
                return ans
            n = n >> 1
        return -ans if flag else ans
# @lc code=end
