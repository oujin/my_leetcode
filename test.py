class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def get_index(string):
            index, map_dict, n = [], {}, 0
            for c in string:
                # print(map_dict.get(c))
                if map_dict.get(c) is None:
                    map_dict[c], n = n, n + 1
                index.append(map_dict[c])
            return index
        
        s_i = get_index(s)
        t_i = get_index(t)
        print(s_i, t_i)
        for si, ti in zip(s_i, t_i):
            if si != ti:
                return False
        return True


s = Solution()
s.isIsomorphic("ab", "aa")