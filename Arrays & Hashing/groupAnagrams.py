class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        res = []
        for s in strs:
            tmp = ''.join(sorted(s))
            if tmp not in mp:
                mp[tmp] = [s]
            else:
                mp[tmp].append(s)
        for key, val in mp.items():
            res.append(val)
        return res
            