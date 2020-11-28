#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, num: int) -> bool:
        if num < 1:
            return False
        for a in [2, 3, 5]:
            if num == 1:
                return True
            while num % a == 0:
                num = num // a
        return num == 1
        
# @lc code=end

