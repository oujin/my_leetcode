class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range((len(nums)-k) // 2):
            nums[i], nums[-i-1-k] = nums[-i-1-k], nums[i]
        print(nums)
        for i in range(k // 2):
            nums[i-k], nums[-i-1] = nums[-i-1], nums[i-k]
        print(nums)
        for i in range(len(nums) // 2):
            nums[i], nums[-i-1] = nums[-i-1], nums[i]


s = Solution()
nums = [1,2,3,4,5,6,7]
s.rotate(nums, 3)
print(nums)
