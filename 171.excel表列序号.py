#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        dicts = dict([(c, i+1) for i, c in enumerate(
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ')])
        num = 0
        for c in s:
            num = num * 26 + dicts[c]
        return num
# @lc code=end

