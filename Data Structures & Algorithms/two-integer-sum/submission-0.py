class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_check = {}
        for i, num in enumerate(nums):
            if num in hash_check:
                return [hash_check[num], i]
            hash_check[target-num] = i

        


