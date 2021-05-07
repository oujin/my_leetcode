#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_xor_y, dist = x ^ y, 0
        while x_xor_y:
            dist += x_xor_y & 1
            x_xor_y = x_xor_y >> 1
        return dist
# @lc code=end

