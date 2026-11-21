class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        for i in range(len(nums)):
            if nums[i] in store:
                store[nums[i]] += 1
            else:
                store[nums[i]] = 1
        # print(store)
        
        tester = []
        for key in store:
            tester.append(store[key])
        

        top_k = sorted(tester)[-k:]
        print(top_k)

        ans = []
        for num in top_k:
            for key in store:
                if key not in ans and num == store[key]:
                    ans.append(key)

        return ans
        