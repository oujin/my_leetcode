#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        c_set = set(s)
        n_total, n_unique = len(s), len(c_set)
        if n_unique > n_total / 2:
            return False
        mask_set = set()
        for i in range(n_total // 2):
            mask_set.add(s[i])
            if len(mask_set) < n_unique or (n_total % (i + 1)):
                continue
            is_repeated = True
            for j in range(1, n_total // (i + 1)):
                if s[(i+1)*j:(i+1)*(j+1)] != s[:i+1]:
                    is_repeated = False
                    break
            if is_repeated:
                return True
        return False
            


# @lc code=end

