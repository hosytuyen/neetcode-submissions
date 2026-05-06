class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1] * len(nums)
        prefix = 1
        for i in range(0, len(nums)):
            prefix_product[i] = prefix
            prefix = prefix * nums[i]
        
        suffix_product = [1] * len(nums)
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            suffix_product[i] = suffix
            suffix = suffix * nums[i]
        
        output = [x*y for x, y in zip(suffix_product, prefix_product)]
        return output
        
        # all_product_nozero = 1
        # zero_index = []
        # for i, num in enumerate(nums):
        #     if num != 0:
        #         all_product_nozero *= num
        #     else:
        #         zero_index.append(i)

        # zero_count = len(zero_index)
        
        # output = []
        # for i, num in enumerate(nums):
        #     if num != 0:
        #         if zero_count > 0:
        #             product_not_self = 0
        #         else:
        #             product_not_self = int(all_product_nozero/num)
        #     else:
        #         if zero_count > 1:
        #             product_not_self = 0
        #         else:
        #             product_not_self = int(all_product_nozero)
        #     output.append(product_not_self)

        # return output
        