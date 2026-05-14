class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:
            print(l, r)
            m = l+(r-l)//2
            if target == nums[m]:
                return m
            if nums[l] <= nums[m]:
                if target < nums[l]:
                    l = m+1
                elif target >= nums[l]:
                    if target < nums[m]:
                        r = m-1
                    else:
                        l = m+1
            else:
                if target >= nums[l]:
                    r = m-1
                else:
                    if target > nums[m]:
                        l = m+1
                    else:
                        r = m-1
        return -1

        