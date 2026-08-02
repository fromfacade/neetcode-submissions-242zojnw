class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = []
        for num in nums:
            product = 1
            for n in nums:
                if n == num:
                    continue
                product *= n
            total.append(product)
        
        return total

                
                
            