#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, curr_sum = nums[0], nums[0]
        for i in range(1, len(nums)):
            if curr_sum < 0:
                curr_sum = max(curr_sum, nums[i])
            else:
                curr_sum += nums[i]
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum
# @lc code=end

