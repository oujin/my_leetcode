#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for n in nums:
            if n != val:
                nums[i], i = n, i + 1
        return i


# @lc code=end

