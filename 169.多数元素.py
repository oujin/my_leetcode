#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # n2cnt = dict()
        # for n in nums:
        #     if n2cnt.get(n):
        #         n2cnt[n] += 1
        #     else:
        #         n2cnt[n] = 1
        # m = len(nums) // 2
        # for k, v in n2cnt.items():
        #     if v > m:
        #         return k
        # return None
        # 法二：空间亚线性算法、水库采样法的极端例子
        e, cnt = None, 0
        for n in nums:
            if n == e:
                cnt += 1
            elif cnt <= 0:
                e, cnt = n, 1
            else:
                cnt -= 1
        return e

# @lc code=end
