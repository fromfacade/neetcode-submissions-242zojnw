class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        total = {}

        for i, n in enumerate(nums):
            s = target - n
            if s in total:
                return [total[s], i]
            
            total[n] = i
                