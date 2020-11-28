#
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        a, b = a & 0xFFFFFFFF, b & 0xFFFFFFFF
        while b:
            a, b = a ^ b, ((a & b) << 1) & 0xFFFFFFFF
        
        return a if a < 0x80000000 else ~(a^0xFFFFFFFF)
        
# @lc code=end

