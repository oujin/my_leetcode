#
# @lc app=leetcode.cn id=405 lang=python3
#
# [405] 数字转换为十六进制数
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        n2str = [str(i) for i in range(10)] + ['a', 'b', 'c', 'd', 'e', 'f']
        nh = ''
        while num != 0:
            num, r = num // 16, num % 16
            nh = n2str[r] + nh
            if len(nh) >= 8:
                break
        return nh
        
# @lc code=end

