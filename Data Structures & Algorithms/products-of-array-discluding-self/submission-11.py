import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # result = []

        # for i in range(len(nums)):
        #     val = nums.pop(0)
        #     result.append(math.prod(nums))
        #     nums.append(val)
        # return result

        n = len(nums)
        res = [1] * n

        pre = 1
        for i in range(n):              # res[i] = product of everything left of i
            res[i] = pre
            pre *= nums[i]

        post = 1
        for i in range(n - 1, -1, -1):  # multiply in everything right of i
            res[i] *= post
            post *= nums[i]

        return res



        


