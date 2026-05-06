class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_product_nozero = 1
        zero_index = []
        for i, num in enumerate(nums):
            if num != 0:
                all_product_nozero *= num
            else:
                zero_index.append(i)
        
        output = []
        for i, num in enumerate(nums):
            if num != 0:
                if len(zero_index) > 0:
                    product_not_self = 0
                else:
                    product_not_self = int(all_product_nozero/num)
            else:
                if len(zero_index) > 1:
                    product_not_self = 0
                else:
                    product_not_self = int(all_product_nozero)
            output.append(product_not_self)

        return output
        