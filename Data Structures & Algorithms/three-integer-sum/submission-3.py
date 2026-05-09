class Solution:
    def twoSum(self, nums, k):
        left = 0
        right = len(nums) - 1
        all_cases = []
        while left < right:
            if nums[left] + nums[right] == k:
                all_cases.append([left, right])
            if nums[left] + nums[right] >= k:
                right -= 1
            else:
                left += 1
        return all_cases

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []
        for i in range(len(nums)):
            all_cases = self.twoSum(nums[i+1:], 0-nums[i])
            for case in all_cases:
                triplet = [nums[i], nums[i+case[0]+1], nums[i+case[1]+1]]
                if triplet not in triplets:
                    triplets.append(triplet)
        return triplets

        