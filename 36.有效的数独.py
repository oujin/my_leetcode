#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            cnt_map1 = {}
            cnt_map2 = {}
            for j in range(9):
                if '1' <= board[i][j] <= '9':
                    if board[i][j] in cnt_map1:
                        return False
                    cnt_map1[board[i][j]] = 1
                if '1' <= board[j][i] <= '9':
                    if board[j][i] in cnt_map2:
                        return False
                    cnt_map2[board[j][i]] = 1
        for i in range(3):
            for j in range(3):
                cnt_map = {}
                for m in range(3):
                    for n in range(3):
                        if '1' <= board[i*3+m][j*3+n] <= '9':
                            if board[i*3+m][j*3+n] in cnt_map:
                                return False
                            cnt_map[board[i*3+m][j*3+n]] = 1
        return True
            
# @lc code=end

