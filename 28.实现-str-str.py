#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            h_index, n_index = i, 0
            while True:
                if n_index >= len(needle):
                    return h_index
                if i >= len(haystack):
                    return -1
                if haystack[i] != needle[n_index]:
                    break
                i, n_index = i + 1, n_index + 1
        return 0 if haystack == needle == "" else -1
# @lc code=end

