class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        for left in range(len(heights)-1):
            right = left+1
            while right < len(heights):
                w = right - left
                h = min(heights[left], heights[right])
                current_water = w*h
                # print(w, h, current_water)
                if max_water < current_water:
                    max_water = current_water
                right += 1
        return max_water
        