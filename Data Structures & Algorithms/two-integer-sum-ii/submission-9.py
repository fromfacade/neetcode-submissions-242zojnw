class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, 1

        while r < len(numbers):
            curr = numbers[r] + numbers[l]
            if curr > target:
                r += 1
            elif curr < target:
                l += 1
                if l == r:
                    r += 1
            else:
                return [l+1, r+1]
            
        return []
        

