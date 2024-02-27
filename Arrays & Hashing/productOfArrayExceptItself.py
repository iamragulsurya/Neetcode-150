class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_cnt = 0
        for num in nums:
            if num != 0:
                product *= num
            else:
                zero_cnt += 1
        res = []
        for i in range(len(nums)):
            if zero_cnt == 0:
                res.append(product//nums[i])
            elif zero_cnt == 1 and nums[i] == 0:
                res.append(product)
            else:
                res.append(0)
        return res
