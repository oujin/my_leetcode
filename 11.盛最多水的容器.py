#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start


class Solution:
    def maxArea(self, height):
        n = len(height)
        if max(height) == height[0]:
            return max([i*height[i] for i in range(1, n)])
        if max(height) == height[-1]:
            return max([(n - i - 1)*height[i] for i in range(n-1)])
        i, j = 0, len(height) - 1
        res = min(height[j], height[i]) * (j - i)
        while height[i] < height[j] and i < j:
            res = max(height[i] * (j - i), res)
            i += 1
        res = max(height[j] * (j - i), res)
        while i < j:
            while height[j] < height[i] and i < j:
                res = max(height[j] * (j - i), res)
                j -= 1
            res = max(height[i] * (j - i), res)
            while height[i] < height[j] and i < j:
                res = max(height[i] * (j - i), res)
                i += 1
            res = max(height[j] * (j - i), res)
            j -= 1
        return res
        


# s = Solution()
# print(s.maxArea([8,20,1,2,3,4,5,6]))
# @lc code=end
