#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                k, m = j + 1, len(nums) - 1
                while k < m:
                    if k > j + 1 and nums[k] == nums[k-1]:
                        k += 1
                    elif nums[i] + nums[j] + nums[k] + nums[m] < target:
                        k += 1
                    elif nums[i] + nums[j] + nums[k] + nums[m] == target:
                        res.append([nums[i], nums[j], nums[k], nums[m]])
                        k, m = k + 1, m - 1
                    else:
                        m -= 1
        return res

# @lc code=end
