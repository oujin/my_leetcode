#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        peers = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in ['(', '{', '[']:
                brackets.append(c)
            elif c in [')', '}', ']']:
                if len(brackets) <= 0 or peers[c] != brackets[-1]:
                    return False
                brackets.pop(-1)
        return len(brackets) <= 0

# @lc code=end
