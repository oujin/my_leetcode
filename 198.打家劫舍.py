#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        for i in range(len(nums)-2):
            nums[i+2] += nums[i]
            if nums[i] > nums[i+1]:
                nums[i+1] = nums[i]
        return max([*nums[-2:], 0])
# @lc code=end

