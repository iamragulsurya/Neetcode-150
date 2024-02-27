class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        nums = sorted(list(set(nums)))
        n = len(nums)
        cnt, res = 1, 0
        for i in range(1, n):
            if nums[i] == nums[i-1] + 1:
                cnt += 1
            else:
                res = max(res, cnt)
                cnt = 1
        res = max(res, cnt)
        return res