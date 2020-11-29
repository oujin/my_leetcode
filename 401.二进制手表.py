#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#

# @lc code=start

cnt2num = [[], [], [], [], [], []]
for i in range(60):
    cnt2num[bin(i).count('1')].append(i)

class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        ans = []
        for ni in range(min(num+1, 6)):
            if num - ni > 4:
                continue
            for h in cnt2num[num-ni]:
                if h > 11:
                    break
                for m in cnt2num[ni]:
                    ans.append('{}:{:02d}'.format(h, m))
        return ans

        
# @lc code=end

