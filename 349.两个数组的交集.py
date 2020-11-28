#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1, union = set(nums1), set()
        for n in nums2:
            if not set1:
                break
            if n in set1:
                union.add(n)
                set1.remove(n)
        return list(union)
        
# @lc code=end

