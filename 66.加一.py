#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        digits[i] += 1
        while i and digits[i] // 10:
            digits[i], digits[i-1] = digits[i] % 10, digits[i-1] + 1
            i -= 1
        if digits[i] // 10:
            digits = [1, digits[i] % 10] + digits[i+1:]
        return digits
# @lc code=end

