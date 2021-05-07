#
# @lc app=leetcode.cn id=475 lang=python3
#
# [475] 供暖器
#

# @lc code=start
class Solution:
    def findRadius(self, houses, heaters):
        heaters.sort()
        houses.sort()
        print(heaters)
        print(houses)
        # 每个房子分配最近的加热器
        i, j = 0, 0
        heater_map = []
        while i < len(houses):
            while j < len(heaters) and houses[i] > heaters[j]:
                j += 1
            if j >= len(heaters):
                heater_map.append(abs(heaters[j-1] - houses[i]))
            elif j > 0:
                heater_map.append(min(abs(heaters[j] - houses[i]),abs(heaters[j-1] - houses[i])))
            else:
                heater_map.append(abs(heaters[j] - houses[i]))
            i += 1
        return max(heater_map)
        

# @lc code=end

