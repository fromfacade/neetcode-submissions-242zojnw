class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub, total = deque(), 0
        maxS = nums[0]


        for i in range(len(nums)):
            total += nums[i]
            maxS = max(maxS, total)
            print(maxS)
            sub.append(nums[i])
        print('\n')
        while sub:
            elem = sub.popleft()
            total -= elem
            if total > 0:
                maxS = max(maxS, total)
            print(maxS)
        
        return maxS