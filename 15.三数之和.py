#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums):
        if len(nums) <= 2:
            return []
        nums.sort()
        print(nums)
        res = []
        i, j, k = 0, 1, 2
        while i < len(nums):
            while 0 < i < len(nums) and nums[i] == nums[i-1]:
                i += 1
            j, k = i + 1, len(nums) - 1
            while j < k:
                while i+1 < j < len(nums) and nums[j] == nums[j-1]:
                    j += 1
                while j < k and nums[j] + nums[k] + nums[i] < 0:
                    j += 1
                while j < k and nums[j] + nums[k] + nums[i] > 0:
                    k -= 1
                if j < k and nums[j] + nums[k] + nums[i] == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
            i += 1
                
        return res


# print(Solution().threeSum([-1,0,1,2,-1,-4]))
# @lc code=end

