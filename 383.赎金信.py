#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r2cnt = dict()
        for c in ransomNote:
            r2cnt[c] = r2cnt[c] + 1 if r2cnt.get(c) else 1
        for c in magazine:
            if not r2cnt:
                break
            if r2cnt.get(c):
                r2cnt[c] -= 1
                if r2cnt[c] <= 0:
                    r2cnt.pop(c)
        return not r2cnt

# @lc code=end

