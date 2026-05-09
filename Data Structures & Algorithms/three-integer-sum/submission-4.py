class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []
        # print(nums)
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                c_sum = nums[i] + nums[j] + nums[k]
                c_triplet = [nums[i], nums[j], nums[k]]
                if c_sum == 0:
                    if c_triplet not in triplets:
                        triplets.append(c_triplet)
                if nums[j] + nums[k] >= -nums[i]:
                    k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
        return triplets

        