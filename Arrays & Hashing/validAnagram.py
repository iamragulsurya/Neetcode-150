class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm_1 = {}
        hm_2 = {}
        for ch in s:
            if ch not in hm_1:
                hm_1[ch] = 1
            else:
                hm_1[ch] += 1
        for ch in t:
            if ch not in hm_2:
                hm_2[ch] = 1
            else:
                hm_2[ch] += 1
        return hm_1 == hm_2