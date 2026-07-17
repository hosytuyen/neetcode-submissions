class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)

        for i in range(1, len(nums)):
            output[i] = nums[i-1]*output[i-1]

        output_2 = [1]*len(nums)
        for j in range(len(nums)-2, -1, -1):
            output_2[j] = nums[j+1]*output_2[j+1]
        
        return [output[i] * output_2[i] for i in range(len(output))]
        