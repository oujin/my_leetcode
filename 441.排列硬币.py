#
# @lc app=leetcode.cn id=441 lang=python3
#
# [441] 排列硬币
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = ((1 + 8 * n) ** 0.5 - 1) * 0.5
        return max(int(k), 0)
        
# @lc code=end

