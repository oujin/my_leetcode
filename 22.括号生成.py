#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int):
        if n <= 0:
            return []
        queue = ['(']
        while len(queue[0]) < 2 * n:
            prefix = queue.pop(0)
            if prefix.count('(') < n:
                queue.append(prefix + '(')
            if prefix.count('(') > prefix.count(')'):
                queue.append(prefix + ')')
        return queue


# @lc code=end

