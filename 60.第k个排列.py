#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#

# @lc code=start
class Solution:
    def fact(self, n):
        ans, i = [1], 1
        while i <= n:
            ans.append(ans[-1]*i)
            i += 1
        return ans

    def getPermutation(self, n: int, k: int) -> str:
        if k == 1:
            return ''.join([str(i) for i in range(1, n + 1)])
        facts = self.fact(n)
        if k == facts[0]:
            return ''.join([str(i) for i in range(n, 0, -1)])
        facts = facts[:-1]
        enum = list(range(1, n + 1))
        ans = ''
        for i in range(1, n):
            if (k-1) // facts[n-i] == 0:
                ans = ans + str(enum.pop(0))
                continue
            k, m = k % facts[n-i], (k-1) // facts[n-i]
            ans = ans + str(enum.pop(m))
        ans = ans + str(enum.pop(0))
        return ans

# @lc code=end

