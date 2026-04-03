class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = []
        for i, num in enumerate(nums):
            product = 1
            for j, n in enumerate(nums):
                if i == j:
                    continue
                product *= n
            total.append(product)
        
        return total

                
                
            