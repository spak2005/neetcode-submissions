class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        nums = [-1,0,1,2,-1,-4]
        sorted_nums = [-4,-1,-1,0,1,2]
        """

        sorted_nums = sorted(nums)
        store = []
        seen = set()

        for i in range(len(nums)-1):
            j, k, target = i+1, len(nums)-1,0-sorted_nums[i]
                
            while j < k:
                total = sorted_nums[j] + sorted_nums[k]
                if total > target:
                    k -= 1
                elif total < target:
                    j += 1
                else:
                    if (sorted_nums[i], sorted_nums[j], sorted_nums[k]) not in seen:
                        store.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                        seen.add((sorted_nums[i], sorted_nums[j], sorted_nums[k]))
                    j += 1


        return store
        """

        """

            




        