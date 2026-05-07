class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        num_set = {}
        for num in nums:
            num_set[num] = num+1

        max_length = 1
        for num in nums:
            length = 1
            if num-1 not in num_set:
                while num+length in num_set:
                    length += 1
            if length > max_length:
                max_length = length
        return max_length
        
        # nums = list(sorted(set(nums)))
        # max_len = 1
        # current_max_len = 1
        # for i in range(len(nums)-1):
        #     if nums[i]+1 == nums[i+1]:
        #         current_max_len += 1
        #     else:
        #         if max_len < current_max_len:
        #             max_len = current_max_len
        #         current_max_len = 1
        # if max_len < current_max_len:
        #     max_len = current_max_len        
        # return max_len


