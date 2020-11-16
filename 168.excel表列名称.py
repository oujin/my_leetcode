#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start


class Solution:
    def convertToTitle(self, n: int) -> str:
        dicts = dict([(i+1, c) for i, c in enumerate(
            'ABCDEFGHIJKLMNOPQRSTUVWXY')])
        dicts[0] = 'Z'
        name = ''
        while n > 26:
            name = dicts[n % 26] + name
            if n % 26 == 0:
                n = n // 26 - 1
            else:
                n = n // 26
        return dicts[n % 26] + name
# @lc code=end
