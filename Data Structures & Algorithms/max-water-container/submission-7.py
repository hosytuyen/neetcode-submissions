class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        left = 0
        right = len(heights)-1
        while left < right:
            w = right - left
            h = min(heights[left], heights[right])
            current_water = w*h
            # print(w, h, current_water)
            if max_water < current_water:
                max_water = current_water
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return max_water
        