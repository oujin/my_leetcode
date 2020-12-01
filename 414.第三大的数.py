#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        ans = [None, None, None]
        for n in nums:
            for i in range(3):
                if ans[i] is None:
                    ans[i] = n
                    break
                if n > ans[i]:
                    ans[i], ans[i+1:] = n, ans[i:2]
                    break
                if n == ans[i]:
                    break
        return ans[0] if ans[2] is None else ans[2]
        
# @lc code=end

