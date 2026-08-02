class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = set()
        for i in nums:
            if i in x:
                continue
            else:
                x += i
        return x
