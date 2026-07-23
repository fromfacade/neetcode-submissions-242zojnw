class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        vals = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        print(vals)

        i = 0
        while i < k:
            res.append(vals[i][0])
            i += 1

        return res