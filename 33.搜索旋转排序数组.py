#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) <= 1:
            return 0 if nums[0] == target else -1
        m = len(nums) >> 1
        if (nums[m] <= target <= nums[-1]) or (nums[0] <= nums[m] <= target) or (target < nums[0] <= nums[m]):
            res = self.search(nums[m:], target)
            return res + m if res >= 0 else -1
        if (nums[0] <= target < nums[m]) or (nums[m] <= nums[-1] < target) or (target < nums[m] <= nums[-1]):
            return self.search(nums[:m], target)
        return -1
# @lc code=end

