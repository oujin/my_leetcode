#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            layer = [1]
            if len(triangle) > 0:
                for j in range(i-1):
                    layer.append(triangle[-1][j] + triangle[-1][j+1])
                layer.append(1)
            triangle.append(layer)
        return triangle
# @lc code=end

