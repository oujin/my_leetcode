#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        b, e = 0, len(s)-1
        while b < e:
            s[b], s[e] = s[e], s[b]
            b, e = b + 1, e - 1
# @lc code=end

