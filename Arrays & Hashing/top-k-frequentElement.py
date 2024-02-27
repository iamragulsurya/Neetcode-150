class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        res = []
        for num in nums:
            if num not in mp:
                mp[num] = 1
            else:
                mp[num] += 1
        mp = dict(sorted(mp.items(), key = lambda l: l[1], reverse = True))
        i = 0
        for key, val in mp.items():
            res.append(key)
            i += 1
            if i == k:
                break
        return res