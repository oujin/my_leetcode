#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        if target >= nums[-1]:
            return len(nums) if target > nums[-1] else len(nums) - 1
        s, e, mid = 0, len(nums) - 1, len(nums) // 2
        while True:
            if nums[mid] == target:
                return mid
            elif s == mid:
                return mid if nums[mid] > target else mid + 1
            elif nums[mid] > target:
                e, mid = mid, (mid + s) // 2
            else:
                s, mid = mid, (mid + e) // 2
# @lc code=end

