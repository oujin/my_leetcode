#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#

# @lc code=start


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m == n and nums1[-1] <= nums2[-1]:
            nums1, m = nums1 + nums2[-1:], m + 1
            nums2, n = nums2[:-1], n - 1
        elif m == n:
            nums2, n = nums2 + nums1[-1:], n + 1
            nums1, m = nums1[:-1], m - 1
        if m < n:
            (nums1, m), (nums2, n) = (nums2, n), (nums1, m)
        e = (m + n) // 2
        s = e - 1 + (m + n) % 2
        if n <= 0 or nums1[e] <= nums2[0]:
            nums = nums1 + nums2
            return (nums[s] + nums[e]) / 2.
        if nums2[-1] <= nums1[0]:
            nums = nums2 + nums1
            return (nums[s] + nums[e]) / 2.
        if nums1[e-n] <= nums2[-1] <= nums1[e-n+1]:
            ne = ns = nums2[-1]
            if s != e:
                ns = max(nums1[e-n], nums2[-2]) if n > 1 else nums1[e-n]
            return (ne + ns) / 2.
        p2, c2, m1, m2 = 0, n-1, e-n//2-1, n//2
        while True:
            if nums1[m1] <= nums2[m2] <= nums1[m1+1]:
                ne = ns = nums2[m2]
                if s != e:
                    ns = nums1[m1] if m2 < 1 else max(nums1[m1], nums2[m2-1])
                return (ne + ns) / 2.
            if ((n <= m2+1 or nums1[m1] <= nums2[m2+1]) and
                    (nums2[m2] <= nums1[m1])):
                ne = ns = nums1[m1]
                if s != e:
                    ns = max(nums2[m2], nums1[m1-1])
                return (ne + ns) / 2.
            if p2 == m2:
                p2 = m2 = c2
            elif m2 == c2:
                m2 = c2 = p2
            elif nums1[m1] > nums2[m2]:
                p2, m2 = m2, (m2 + c2) // 2
            elif nums2[m2] > nums1[m1+1]:
                m2, c2 = (p2 + m2) // 2, m2
            m1 = e - m2 - 1


# @lc code=end
