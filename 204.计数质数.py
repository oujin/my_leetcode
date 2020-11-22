#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        i, end, nonPrimes = 2, int(n ** 0.5) + 1, {0, 1}
        for k in range(i, end+1):
            for j in range(k, n // k + 1):
                if k * j < n:
                    nonPrimes.add(k*j)
        return n - len(nonPrimes)
# @lc code=end

