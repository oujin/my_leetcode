#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = dict()
        for c in s:
            if chars.get(c) is None:
                chars[c] = 1
            else:
                chars[c] += 1
        for c in t:
            if not chars.get(c): # None or 0
                return False
            chars[c] -= 1
        return True

# @lc code=end

