class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for curr_ind in range(0, len(nums)-1):
            for oth_ind in range(curr_ind+1, len(nums)):
                if nums[curr_ind] == nums[oth_ind]:
                    return True
        
        return False
        