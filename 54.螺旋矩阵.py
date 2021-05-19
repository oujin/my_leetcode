#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]], direction='right') -> List[int]:
        if len(matrix) <= 0 or len(matrix[0]) <= 0:
            return []
        if direction == 'right':
            return matrix[0] + self.spiralOrder(matrix[1:], 'down')
        if direction == 'down':
            return [row[-1] for row in matrix] + self.spiralOrder(
                [row[:-1] for row in matrix], 'left'
            )
        if direction == 'left':
            return matrix[-1][::-1] + self.spiralOrder(matrix[:-1], 'up')
        if direction == 'up':
            return [row[0] for row in matrix[::-1]] + self.spiralOrder(
                [row[1:] for row in matrix], 'right'
            )
        
# @lc code=end

