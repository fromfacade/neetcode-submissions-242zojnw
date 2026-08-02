class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        freq = 0
        
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        elems = list(count.keys())
        while freq != k:
            if max(elems) not in res:
                res.append(max(elems))
                elems.remove(max(elems))
                freq += 1
        
                
        return res
            
        #return the highest k value(s) of hashmap
        #how can I do this with a hashmap 