#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n2index = dict()
        for j, n in enumerate(nums):
            i = n2index.get(n)
            if i is not None:
                if j - i <= k:
                    return True
            n2index[n] = j
        return False


# @lc code=end

