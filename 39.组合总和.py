#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(
            [i for i in candidates if i <= target], reverse=True)

        def combine(array, t):
            if (len(array) == 1 and t % array[0]) or not array:
                return []
            if len(array) == 1:
                return [[array[0]] * (t // array[0])]
            ans = []
            if array[0] == t:
                ans.append([array[0]])
            # 用第一个元素
            i = 0
            while i < len(array):
                if array[i] <= t - array[0]:
                    break
                i += 1
            res = combine(array[i:], t-array[0])
            for r in res:
                ans.append([array[0]] + r)
            # print(array)
            # 不用第一个元素
            return ans + combine(array[1:], t)
        
        return combine(candidates, target)
# @lc code=end

