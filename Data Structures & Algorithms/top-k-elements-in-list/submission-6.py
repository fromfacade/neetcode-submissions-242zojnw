class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        elems, res = [], []

        for num, cnt in freq.items():
            elems.append([cnt, num])
        elems.sort()
        
        while len(res) != k:
            res.append(elems.pop()[1])

        return res
        
        
        
