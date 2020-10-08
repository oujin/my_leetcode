#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c, res = 0, ''
        ia, ib = a[::-1], b[::-1]
        for ai, bi in zip(ia, ib):
            r = (int(ai) + int(bi) + c) % 2
            c = (int(ai) + int(bi) + c) // 2
            res = f'{res}{r}'
        remain = ia[len(res):] if ia[len(res):] else ib[len(res):]
        for n in remain:
            r = (int(n) + c) % 2
            c = (int(n) + c) // 2
            res = f'{res}{r}'
        res = f'{res}{c}' if c else res
        return res[::-1]

        
# @lc code=end

