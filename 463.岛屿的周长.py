#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        circle_len = 0
        for i, row in enumerate(grid):
            for j, n in enumerate(row):
                if n == 0:
                    continue
                if n == 1 and (i == 0 or grid[i-1][j] == 0):
                    # 上方
                    circle_len += 1
                if n == 1 and (i == len(grid)-1 or grid[i+1][j] == 0):
                    # 下方
                    circle_len += 1
                if n == 1 and (j == 0 or row[j-1] == 0):
                    # 左边
                    circle_len += 1
                if n == 1 and (j == len(row)-1 or row[j+1] == 0):
                    # 右边
                    circle_len += 1
        return circle_len
# @lc code=end

