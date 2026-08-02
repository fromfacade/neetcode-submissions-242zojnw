class Solution:
    def findMin(self, nums: List[int]) -> int:
        prev = 0
        for c in nums:
            if prev > c:

                return c
            else:
                prev = c

        return c