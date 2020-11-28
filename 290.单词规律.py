#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(' ')
        if len(s_list) != len(pattern):
            return False
        p2s, s2p = dict(), dict()
        for i in range(len(pattern)):
            if p2s.get(pattern[i]) is None:
                p2s[pattern[i]] = s_list[i]
            elif p2s.get(pattern[i]) != s_list[i]:
                return False
            if s2p.get(s_list[i]) is None:
                s2p[s_list[i]] = pattern[i]
            elif s2p.get(s_list[i]) != pattern[i]:
                return False
        return True

# @lc code=end

