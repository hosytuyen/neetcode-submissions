class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]*len(nums)
        for i in range(1, len(nums)):
            pre[i] = nums[i-1]*pre[i-1]

        print(pre)
        suf = 1
        for j in range(len(nums)-2, -1, -1):
            suf = nums[j+1]*suf
            pre[j] = pre[j]*suf
        
        return pre
        