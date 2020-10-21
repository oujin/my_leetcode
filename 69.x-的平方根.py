#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        s, y, e = 0, x, x
        y2_dict = dict()
        while y > 0:
            y2 = y2_dict.get(y) or y ** 2
            if y2 == x:
                return y
            if s + 1 >= e:
                return s
            y2_dict[y] = y2
            if y2 < x:
                y, s = (e + y) // 2, y
            else:
                y, e = (s + y) // 2, y
        return y
# @lc code=end

