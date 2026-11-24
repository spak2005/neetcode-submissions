class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        height = [1,7,2,5,4,7,3,6]
        height = [1,2,7,5,4,7,3,6]
        """

        vol = 1
        max_vol = 0
        store=[]

        # for i in range(len(heights)):
        #     for j in range(i, len(heights)):
        #         vol = min(heights[i], heights[j]) * (j-i)
        #         store.append(vol)
        #         max_vol = max(max_vol, vol)
        # return max_vol

        i, j = 0, len(heights)-1

        while i < j:
            vol = min(heights[i], heights[j]) * (j-i)
            max_vol = max(max_vol, vol)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return max_vol

