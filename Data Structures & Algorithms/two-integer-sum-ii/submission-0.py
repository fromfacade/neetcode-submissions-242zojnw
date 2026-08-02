class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, 1

        while r < len(numbers):
            curr = numbers[r] + numbers[l]
            if curr == target:
                return [l+1, r+1] 
            
            if curr > target:
                r += 1
            else:
                l += 1
        
        return

