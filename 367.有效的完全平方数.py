#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        s, e = 1, num
        while s < e:
            s, e = s * 2, e // 2 + 1
        if s == e and s * e == num:
            return True
        for i in range(e, s):
            if i * i == num:
                return True
            if i * i > num:
                return False
        return False
# @lc code=end

