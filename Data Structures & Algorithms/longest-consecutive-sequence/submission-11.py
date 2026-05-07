class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        num_set = set(nums)

        max_length = 1
        for num in num_set:
            length = 1
            if num-1 not in num_set:
                while num+length in num_set:
                    length += 1
            if length > max_length:
                max_length = length
        return max_length


