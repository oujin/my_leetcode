#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def add(self, num1, num2, c):
        if (not num1 or not num2) and not c:
            return num1 + num2
        if not num1 and not num2:
            return str(c) if c else ''
        if not num1:
            num1, num2 = num2, num1
        ans, c = str((int(num1[-1]) + c) % 10), (int(num1[-1]) + c) // 10
        if num2:
            res = int(ans) + int(num2[-1])
            ans, c = str(res % 10), c + (res // 10)
        return self.add(num1[:-1], num2[:-1], c) + ans

    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        ans = ''
        for n in num2:
            ans = ans + '0'
            for _ in range(int(n)):
                ans = self.add(ans, num1, 0)
        return '0' if not ans else ans

# @lc code=end

