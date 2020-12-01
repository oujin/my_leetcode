#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        c2cnt = dict()
        for c in s:
            c2cnt[c] = c2cnt[c] + 1 if c2cnt.get(c) else 1
        n, r = 0, 0
        for k, v in c2cnt.items():
            if v > 1:
                n += (v // 2) * 2
            if v % 2:
                r = 1
        return n + r
# @lc code=end

