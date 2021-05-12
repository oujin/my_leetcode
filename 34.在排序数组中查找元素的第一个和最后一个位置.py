#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or nums[0] > target or nums[-1] < target:
            return [-1, -1]
        if len(nums) <= 1:
            return [0, 0]
        m = len(nums) >> 1
        l_res = self.searchRange(nums[:m], target)
        r_res = self.searchRange(nums[m:], target)
        if r_res[0] >= 0:
            r_res[0], r_res[1] = r_res[0] + m, r_res[1] + m
        res = []
        if l_res[0] >= 0 and r_res[0] >= 0:
            res = [l_res[0], r_res[1]]
        else:
            res = l_res if l_res[0] >= 0 else r_res
        return res
        
# @lc code=end

