#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        last_layer = []
        for i in range(rowIndex+1):
            layer = [1]
            if i > 0:
                for j in range(i-1):
                    layer.append(last_layer[j] + last_layer[j+1])
                layer.append(1)
            last_layer = layer
        return last_layer
# @lc code=end

