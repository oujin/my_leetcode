#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        if n <= 0:
            return False
        tmp = set()
        
        def get_new_n(num):
            res = 0
            while num:
                res += (num % 10) ** 2
                num //= 10
            return res
        
        while n > 1 and n not in tmp:
            tmp.add(n)
            n = get_new_n(n)
        return n == 1

# @lc code=end
