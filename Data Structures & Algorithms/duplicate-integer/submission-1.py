class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        trace = {}
        for num in nums:
            if num in trace:
                trace[num] += 1
            else:
                trace[num] = 1

        for num, count in trace.items():
            if count > 1:
                return True
        
        return False
        