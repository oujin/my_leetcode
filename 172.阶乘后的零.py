#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = n = n // 5
        while n > 0:
            cnt, n = cnt + n // 5, n // 5
        return cnt

# @lc code=end

