class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            l1 = stones.heappop(stones)
            l2 = stones.heappop(stones)
            if l1 == l2:
                continue
            if l1 > l2:
                heapq.heappush(stones, (l1 - l2) * -1)
            else: 
                heapq.heappush(stones, (l2 - l1) * -1)

        print(stones)  