class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_dist, dist = 1, 1
        sorted_nums = sorted(nums)
        print(sorted_nums)

        if not nums: return 0

        for i in range(1, len(nums)):
            diff = sorted_nums[i]-sorted_nums[i-1]
            if diff == 0:
                continue
            elif diff == 1:
                dist+=1
                max_dist = max(max_dist, dist)
            else:
                dist = 1
        return max_dist 
