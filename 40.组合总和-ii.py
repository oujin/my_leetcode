#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(
            [i for i in candidates if i <= target], reverse=True)

        def combine(array, t):
            if (len(array) == 1 and t != array[0]) or not array:
                return []
            ans = []
            if len(array) == 1:
                return [[array[0]]]
            if array[0] == t:
                ans.append([array[0]])
            # 用第一个元素
            i = 1
            while i < len(array):
                if array[i] <= t - array[0]:
                    break
                i += 1
            res = combine(array[i:], t-array[0])
            for r in res:
                ans.append([array[0]] + r)
            # print(array)
            # 不用第一个元素
            j = 1
            for j in range(1, len(array)):
                if array[j] != array[j-1]:
                    break
            if array[j] != array[j-1]:
                return ans + combine(array[j:], t)
            return ans
        
        return combine(candidates, target)
# @lc code=end

