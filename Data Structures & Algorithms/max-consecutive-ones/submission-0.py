class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        m = 0

        for num in nums:
            if num == 1:
                curr += 1
                m = max(curr, m)
            else:
                curr = 0
        
        return m