#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) <= 1:
            return '' if len(strs) <= 0 else strs[0]
        if len(strs) == 2:
            pref = ''
            for i, j in zip(*strs):
                if i != j:
                    return pref
                pref = pref + i
            return pref
        m = len(strs) // 2
        return self.longestCommonPrefix([
            self.longestCommonPrefix(strs[:m]),
            self.longestCommonPrefix(strs[m:])])
# @lc code=end
