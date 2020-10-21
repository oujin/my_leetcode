#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        res, last = 1, 1
        for k in range(n // 2):
            last = last * (n - 2 * k) * (n - 2* k - 1) / (n - k) / (k + 1)
            res += last
        return int(res)
# @lc code=end

