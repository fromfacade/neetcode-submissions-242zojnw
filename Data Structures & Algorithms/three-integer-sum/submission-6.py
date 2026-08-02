class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    s = nums[i] + nums[j] + nums[k] 
                    if s == 0:
                        res.add(tuple([nums[i], nums[j], nums[k]]))
        
        return [list(i) for i in res]