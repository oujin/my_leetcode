#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 0:
            return []
        if len(nums) <= 1:
            return [nums]
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            right = self.permuteUnique(nums[:i] + nums[i+1:])
            for r in right:
                ans.append([nums[i], *r])
        return ans
# @lc code=end

