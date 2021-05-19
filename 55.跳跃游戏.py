#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index = nums[0]
        i = 0
        while i < len(nums) and index < len(nums)-1 and i < index:
            i += 1
            index = max(i+nums[i], index)
        return index >= len(nums) - 1
# @lc code=end

