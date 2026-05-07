class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums = list(sorted(set(nums)))
        max_len = 1
        current_max_len = 1
        print(nums)
        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                current_max_len += 1
            else:
                if max_len < current_max_len:
                    max_len = current_max_len
                current_max_len = 1
        if max_len < current_max_len:
            max_len = current_max_len        
        return max_len


