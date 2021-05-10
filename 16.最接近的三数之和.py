#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k:
                while nums[i] + nums[j] + nums[k] >= target and j < k:
                    if (nums[i] + nums[j] + nums[k] - target) < abs(res - target):
                        res = nums[i] + nums[j] + nums[k]
                    if res == target:
                        return res
                    k -= 1
                if j < k:
                    if (target - nums[i] - nums[j] - nums[k]) < abs(res - target):
                        res = nums[i] + nums[j] + nums[k]
                    if res == target:
                        return res
                j += 1
        return res
# @lc code=end

