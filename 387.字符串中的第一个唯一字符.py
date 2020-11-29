#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s2cnt =  dict()
        for c in s:
            s2cnt[c] = s2cnt[c] + 1 if s2cnt.get(c) else 1
        for i, c in enumerate(s):
            if s2cnt[c] <= 1:
                return i
        return -1
# @lc code=end

