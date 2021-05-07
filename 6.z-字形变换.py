#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        m = (len(s) - 1) // (2 * numRows - 2) + 1
        tmp = [' '] * 2 * numRows * m
        for i in range(0, 2*m, 2):
            sl = len(s[(numRows-1)*i:(numRows-1)*(i+1)+1])
            tmp[numRows*i:numRows*i+sl] = s[(numRows-1)*i:(numRows-1)*(i+1)+1]
            sl = len(s[(numRows-1)*(i+1)+1:(numRows-1)*(i+2)])
            tmp[numRows*(i+1)+1:numRows*(i+1)+1+sl] = s[(numRows-1)*(i+1)+1:(numRows-1)*(i+2)]
            tmp[numRows*(i+1):numRows*(i+2)] = tmp[numRows*(i+1):numRows*(i+2)][::-1]
        string = ''
        for i in range(numRows):
            string = string + ''.join([tmp[j * numRows + i] for j in range(2*m)])
        return string.replace(' ', '')
        
# @lc code=end

