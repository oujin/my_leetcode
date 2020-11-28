#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        s, m, e = 1, (1+n)//2, n
        while s < m < e:
            if isBadVersion(m):
                m, e = (m + s)//2, m
            else:
                s, m = m, (m+e)//2
        return m + 1

        
# @lc code=end

