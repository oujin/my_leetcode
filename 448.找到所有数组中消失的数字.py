#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 1
        while i <= len(nums):
            n = nums[i-1]
            if nums[i-1] == i or nums[n-1] == nums[i-1]:
                i += 1
            else:
                nums[i-1], nums[n-1] = nums[n-1], nums[i-1]
        return [i for i, n in enumerate(nums, 1) if i != n]


        
# @lc code=end

