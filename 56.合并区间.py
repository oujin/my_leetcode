#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        for inter in intervals[1:]:
            if inter[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], inter[1])
            else:
                ans.append(inter)
        return ans
# @lc code=end

