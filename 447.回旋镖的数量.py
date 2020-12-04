#
# @lc app=leetcode.cn id=447 lang=python3
#
# [447] 回旋镖的数量
#

# @lc code=start
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        dist2peers = dict()
        for i, p1 in enumerate(points):
            for j, p2 in enumerate(points[i+1:], i+1):
                dist = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
                if dist2peers.get(dist):
                    dist2peers[dist].append([i, j])
                else:
                    dist2peers[dist] = [[i, j]]
        cnt = 0
        for _, peers in dist2peers.items():
            for i, p1 in enumerate(peers):
                for p2 in peers[i+1:]:
                    if p2[0] in p1 or p2[1] in p1:
                        cnt += 2
        return cnt

# @lc code=end

