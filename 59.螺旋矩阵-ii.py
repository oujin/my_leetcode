#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def generate(matrix, n, direction='left'):
            if n <= 0:
                return matrix
            if direction == 'left':
                for row in matrix:
                    row.insert(0, n)
                    n -= 1
                matrix.append([n-i for i in range(len(matrix[0]))])
                return generate(matrix, n-len(matrix[0]), 'right')
            if direction == 'right':
                for row in matrix[::-1]:
                    row.append(n)
                    n -= 1
                matrix.insert(0, [n-i for i in range(len(matrix[-1]))][::-1])
                return generate(matrix, n-len(matrix[0]), 'left')
        
        direction = 'left' if n % 2 else 'right'
        return generate([[n*n]], n*n-1, direction)


# @lc code=end

