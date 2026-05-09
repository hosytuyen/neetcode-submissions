class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []
        print(nums)
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                if nums[j] + nums[k] >= -nums[i]:
                    k -= 1
                if nums[j] + nums[k] < -nums[i]:
                    j += 1
        return triplets

        