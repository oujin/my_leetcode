#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        # nums.sort()
        if len(nums) <= 2:
            return [nums, nums[::-1]]
        ans = []
        for i in range(len(nums)):
            right = self.permute(nums[:i] + nums[i+1:])
            for r in right:
                ans.append([nums[i], *r])
        return ans
# @lc code=end

