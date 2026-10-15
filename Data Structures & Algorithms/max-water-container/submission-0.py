class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxWater = 0
        l = 0
        r = len(heights) - 1
        while r > l:
            maxWater = max(maxWater, min(heights[l], heights[r]) * (r-l))
            
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                

        return maxWater