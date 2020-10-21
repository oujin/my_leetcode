#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        for k in nums2:
            while True:
                if (m <= i) or (nums1[m-1] < k):
                    nums1[m] = k
                    i = m = m + 1
                    break
                elif nums1[i] >= k:
                    nums1[i+1:m+1] = nums1[i:m]
                    nums1[i] = k
                    i, m = i + 1, m + 1
                    break
                elif nums1[i] < k <= nums1[i+1]:
                    nums1[i+2:m+1] = nums1[i+1:m]
                    nums1[i+1] = k
                    i, m = i + 1, m + 1
                    break
                else:
                    i = i + 1
# @lc code=end

