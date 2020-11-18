#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        # # 法1，时间O(kn)
        # for _ in range(k):
        #     tmp = nums[-1]
        #     for i in range(len(nums)-1):
        #         nums[-i-1] = nums[-i-2]
        #     nums[0] = tmp
        # 法2，时间O(n)
        for i in range((len(nums)-k) // 2):
            nums[i], nums[-i-1-k] = nums[-i-1-k], nums[i]
        for i in range(k // 2):
            nums[i-k], nums[-i-1] = nums[-i-1], nums[i-k]
        for i in range(len(nums) // 2):
            nums[i], nums[-i-1] = nums[-i-1], nums[i]

# @lc code=end

