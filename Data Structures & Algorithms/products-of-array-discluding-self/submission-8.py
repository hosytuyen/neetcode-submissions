class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]*len(nums)
        for i in range(1, len(nums)):
            pre[i] = nums[i-1]*pre[i-1]

        suf = [1]*len(nums)
        for j in range(len(nums)-2, -1, -1):
            suf[j] *= nums[j+1]*suf[j+1]
        
        return [pre[i]*suf[i] for i in range(len(pre))]
        