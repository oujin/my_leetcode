#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        flag = [-1] * len(s)
        for i, c in enumerate(s):
            for j in range(i+1, len(s)):
                if s[j] == c:
                    flag[j] = i
                    break
        i, j, max_len = 0, 1, 1
        while j < len(s):
            if flag[j] >= i:
                max_len = max(max_len, j-i)
                i = flag[j] + 1
            j += 1
        else:
            max_len = max(max_len, j-i)
        return max_len
# @lc code=end

