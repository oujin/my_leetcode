#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def sort(self, arr):
        if not arr:
            return []
        left, right = [], []
        for i in arr[1:]:
            if i < arr[0]:
                left.append(i)
            else:
                right.append(i)
        return self.sort(left) + arr[:1] + self.sort(right)

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # g, s = self.sort(g), self.sort(s)
        g, s = sorted(g), sorted(s)
        i = 0
        for size in s:
            if len(g) <= i:
                break
            if g[i] <= size:
                i = i + 1
                continue
        return i


# @lc code=end

