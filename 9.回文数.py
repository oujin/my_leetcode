#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        z, y = abs(x), 0
        while z:
            z, y = z // 10, y * 10 + z % 10
        y = y if x >= 0 else -y
        return y == x
# @lc code=end
