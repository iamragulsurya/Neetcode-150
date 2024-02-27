class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        n = len(nums)
        for i in range(n):
            hm[nums[i]] = i
        for i in range(n):
            if target-nums[i] in hm and hm[target-nums[i]] != i:
                return [hm[target-nums[i]], i]
        return []