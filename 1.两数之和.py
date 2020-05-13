#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start


class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        # # # 排序法
        # # # 排序复杂度太高
        # # sort(nums)
        # # while begin < end and not done:
        # #     end, done = bisection_search(nums[begin])
        # def sort(lis):
        #     indice = [i for i in range(len(lis))]
        #     for i in range(len(lis)):
        #         for j in range(0, len(lis) - i - 1):
        #             if lis[j] > lis[j+1]:
        #                 lis[j], lis[j+1] = lis[j+1], lis[j]
        #                 indice[j], indice[j+1] = indice[j+1], indice[j]
        #     return lis, indice

        # def bis_search(sorted_list, t):
        #     # print(sorted_list)
        #     if len(sorted_list) < 1:
        #         return -1, False
        #     mid = len(sorted_list) // 2
        #     if sorted_list[mid] == t:
        #         return mid, True
        #     if sorted_list[mid] < t:
        #         res, done = bis_search(sorted_list[mid+1:], t)
        #         return mid + 1 + res, done
        #     if sorted_list[mid] > t:
        #         return bis_search(sorted_list[:mid], t)

        # sorted_nums, indices = sort(nums)
        # begin, end = 0, len(sorted_nums)
        # # print(sorted_nums)
        # while begin < end:
        #     end, done = bis_search(
        #         sorted_nums[begin+1:end], target - sorted_nums[begin])
        #     # print(indices[begin], indices[end+1], done)
        #     end += 1 + begin
        #     # print(begin, end, done)
        #     if done:
        #         return [indices[begin], indices[end]]
        #     else:
        #         begin += 1
        #         end += 1
        # return []

        # # 哈希法
        h_nums = {}
        for i, n in enumerate(nums):
            h_nums[target - n] = i
        for i, n in enumerate(nums):
            if n in h_nums and i != h_nums[n]:
                return [i, h_nums[n]]
        return []

# @lc code=end