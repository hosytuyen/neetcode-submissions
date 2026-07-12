class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_ = {}
        for i, num in enumerate(nums):
            if num in map_:
                return [map_[num], i]
            map_[target-num] = i
        