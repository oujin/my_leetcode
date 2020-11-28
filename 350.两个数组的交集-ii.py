#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n2cnt = dict()
        for n in nums1:
            if n2cnt.get(n):
                n2cnt[n] += 1
            else:
                n2cnt[n] = 1
        ans = []
        for n in nums2:
            if not n2cnt:
                break
            if n2cnt.get(n):
                ans.append(n)
                n2cnt[n] -= 1
                if n2cnt[n] <= 0:
                    n2cnt.pop(n)
        return ans
        
# @lc code=end

