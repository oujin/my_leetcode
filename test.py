
class Solution:
    def reverse(self, x):
        x, y, s = abs(x), 0, int(x < 1)
        while x:
            print(x // 10, y * 10 + x % 10)
            x, y = x // 10, y * 10 + x % 10
        y *= (-1) ** s
        return y if -2**31 <= y < 2**31-1 else 0


s = Solution()
print(s.reverse(-123))
