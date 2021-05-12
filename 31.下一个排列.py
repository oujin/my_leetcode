#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i >= 1:
            if nums[i] > nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                break
            i -= 1
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j] <= nums[i-1]:
                nums[j], nums[i-1] = nums[i-1], nums[j]
            else:
                break
        for j in range(i, len(nums)-1):
            if nums[j] < nums[j+1]:
                nums[j+1], nums[j] = nums[j], nums[j+1]
            else:
                break
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1

# @lc code=end

