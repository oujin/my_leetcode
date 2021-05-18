#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_map = dict()
        for string in strs:
            s = ''.join(sorted(list(string)))
            if string_map.get(s):
                string_map[s].append(string)
            else:
                string_map[s] = [string]
        return list(string_map.values())

# @lc code=end

