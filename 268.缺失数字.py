#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 缺失数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            ans ^= n
        for n in range(len(nums)+1):
            ans ^= n
        return ans
# @lc code=end

