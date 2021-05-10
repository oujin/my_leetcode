#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start


class Solution:
    num2letter = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                  '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ans = list(self.num2letter[digits[-1]])
        if len(digits) == 1:
            return ans
        for i in range(len(digits)-2, -1, -1):
            res = []
            for let in self.num2letter[digits[i]]:
                for a in ans:
                    res.append(let + a)
            ans = res
        return ans


        # @lc code=end
