#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            if i % 3 == 0:
                if i % 5:
                    ans.append('Fizz')
                else:
                    ans.append('FizzBuzz')
                continue
            if i % 5:
                ans.append(str(i))
            else:
                ans.append('Buzz')
        return ans   
# @lc code=end

