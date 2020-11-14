#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 0:
            return 0
        p_min, p_max, delta = prices[0], prices[0], 0
        for p in prices[1:]:
            if p <= p_min:
                p_min = p_max = p
            elif p > p_max:
                p_max, delta = p, max(delta, p - p_min)
        return delta
# @lc code=end

