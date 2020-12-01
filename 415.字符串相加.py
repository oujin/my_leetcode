#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        c, ans = '0', ''
        
        def str_add(c1, c2):
            s = ord(c1) + ord(c2) - ord('0')
            if s > ord('9'):
                return '1', chr(s - 10)
            else:
                return '0', chr(s)
 
        for n1, n2 in zip(num1[::-1], num2[::-1]):
            if c != '0':
                c, n1 = str_add(n1, c)
            c2, r2 = str_add(n1, n2)
            if c2 != '0':
                _, c = str_add(c, c2)
            ans = ans + r2
        if len(num1) > len(num2):
            max_n, begin = num1, len(num2)  
        else:
            max_n, begin = num2, len(num1) 
        for i in range(begin, len(max_n)):
            if c == '0':
                ans = ans + max_n[::-1][i:]
                break
            c, r = str_add(c, max_n[::-1][i])
            ans = ans + r
        if c != '0':
            ans = ans + c
        return ans[::-1]
        
# @lc code=end

