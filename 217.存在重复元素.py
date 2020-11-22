#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n_set = set()
        for n in nums:
            if n in n_set:
                return True
            n_set.add(n)
        return False
# @lc code=end

