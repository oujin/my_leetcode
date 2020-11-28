#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        b, e = 0, len(s)-1
        while b < e:
            if s_list[b].lower() not in vowels:
                b += 1
            elif s_list[e].lower() not in vowels:
                e -= 1
            else:
                s_list[b], s_list[e] = s_list[e], s_list[b]
                b, e = b + 1, e - 1
        return ''.join(s_list)
        
# @lc code=end

