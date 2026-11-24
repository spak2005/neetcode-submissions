class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_dist, dist, nums_set = 1, 0, set(nums)
        if not nums: return 0
        for x in nums_set:
            if x-1 not in nums_set:
                dist = 0
                j = x
                while j in nums_set:
                    dist+=1
                    max_dist = max(max_dist, dist)
                    j+=1
            else:
                continue
        return max_dist
                


