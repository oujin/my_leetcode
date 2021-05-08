#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start


class Solution:
    def intToRoman(self, num: int) -> str:
        a, num = num // 1000, num % 1000
        b, num = num // 500, num % 500
        c, num = num // 100, num % 100
        d, num = num // 50, num % 50
        e, num = num // 10, num % 10
        f, num = num // 5, num % 5
        res = ('M' * a + 'D' * b + 'C' * c + 'L' * d + 'X' * e +
               'V' * f + 'I' * num)
        return res.replace('DCCCC', 'CM').replace('CCCC', 'CD')\
            .replace('LXXXX', 'XC').replace('XXXX', 'XL')\
            .replace('VIIII', 'IX').replace('IIII', 'IV')
        return res

# @lc code=end
