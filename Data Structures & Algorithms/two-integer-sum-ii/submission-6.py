class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     diff = target - numbers[i]
        #     if diff in set(numbers[i: len(numbers)]):
        #         return [i+1, 1+(numbers.index(diff, i+1))]


        i, j = 0, len(numbers)-1

        while i != j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i+1, j+1]


        