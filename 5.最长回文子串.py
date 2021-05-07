#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = s[0]
        i = 1
        while i < len(s):
            j, k = i-1, i
            while j >= 0 and k < len(s) and s[j] == s[k]:
                j, k = j - 1, k + 1
            if (k - j - 1) > len(palindrome):
                palindrome = s[j+1:k]
            j = k = i
            while j >= 0 and k < len(s) and s[j] == s[k]:
                j, k = j - 1, k + 1
            if (k - j - 1) > len(palindrome):
                palindrome = s[j+1:k]
            i += 1
        return palindrome
                
# s = Solution()
# print(s.longestPalindrome('aaaa'))
# @lc code=end

