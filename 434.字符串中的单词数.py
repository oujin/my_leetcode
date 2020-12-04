#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        cnt, last_is_space = 0, True
        for c in s:
            if c == ' ' and not last_is_space:
                cnt, last_is_space = cnt + 1, True
            elif c != ' ':
                last_is_space = False
        return cnt + (1 - last_is_space)
# @lc code=end

