import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # result = []

        # for i in range(len(nums)):
        #     val = nums.pop(0)
        #     result.append(math.prod(nums))
        #     nums.append(val)
        # return result

        post_fix, pre_fix = [], []
        post_prod, pre_prod = 1, 1

        for num in nums[::-1]:
            post_prod *= num
            post_fix.append(post_prod)

        for num in nums:
            pre_prod *= num
            pre_fix.append(pre_prod)

        res = []
        post_fix = post_fix[::-1]
        for i in range(len(nums)):
            if i > 0 and i < len(nums)-1:
                res.append(pre_fix[i-1]*post_fix[i+1])
            elif i==0:
                res.append(1*post_fix[i+1])
            elif i == (len(nums)-1):
                res.append(pre_fix[i-1]*1)
        return res



        


