class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        total = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in total:
                return [total[diff], i]
            
            total[n] = i