#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        p1, p2 = 0, 1
        while p2 < len(nums):
            if nums[p2] == 0:
                p2 += 1
            elif nums[p1] != 0:
                p2 = p2 + 1 if p1 + 1 >= p2 else p2
                p1 += 1
            else:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1, p2 = p1 + 1, p2 + 1
                
# @lc code=end

