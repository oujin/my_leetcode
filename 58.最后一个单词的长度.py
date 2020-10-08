#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_cnt, cnt = 0, 0
        for c in s:
            last_cnt = cnt if c == ' ' and cnt > 0 else last_cnt
            cnt = 0 if c == ' ' else cnt + 1
        return cnt if cnt != 0 else last_cnt
# @lc code=end

