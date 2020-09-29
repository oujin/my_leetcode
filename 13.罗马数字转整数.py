#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start


class Solution:
    def romanToInt(self, s: str) -> int:
        str2num = {"I": 1, "V": 5, "X": 10,
                   "L": 50, "C": 100, "D": 500, "M": 1000}
        str2id = {"I": 0, "V": 1, "X": 2, "L": 3, "C": 4, "D": 5, "M": 6}
        if len(s) <= 0 or str2num.get(s[0]) is None:
            return 0
        elif len(s) <= 1:
            return str2num.get(s)
        if str2id[s[0]] < str2id[s[1]]:
            return -str2num[s[0]] + str2num[s[1]] + self.romanToInt(s[2:])
        return str2num[s[0]] + self.romanToInt(s[1:])
# @lc code=end
