#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 1:
            return '1'
        last = self.countAndSay(n-1)
        res, cnt, prev = '', 0, last[0]
        for n in last:
            if n == prev:
                cnt += 1
            else:
                res = f'{res}{cnt}{prev}'
                prev, cnt = n, 1
        return f'{res}{cnt}{prev}'
# @lc code=end

