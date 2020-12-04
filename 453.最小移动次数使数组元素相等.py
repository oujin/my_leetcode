#
# @lc app=leetcode.cn id=453 lang=python3
#
# [453] 最小移动次数使数组元素相等
#

# @lc code=start
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n_min, n_sum = nums[0], nums[0]
        for n in nums[1:]:
            if n < n_min:
                n_min = n
            n_sum += n
        return n_sum - n_min * (len(nums))
        
# @lc code=end

