class Solution:
    def findDisappearedNumbers(self, nums):
        i = 1
        while i <= len(nums):
            n = nums[i-1]
            if nums[i-1] == i or nums[n-1] == nums[i-1]:
                i += 1
            else:
                nums[i-1], nums[n-1] = nums[n-1], nums[i-1]
        ans = []
        for i, n in enumerate(nums, 1):
            if i != n:
                ans.append(i)
        return ans


s = Solution()

s.findDisappearedNumbers([4,3,2,7,8,2,3,1])
