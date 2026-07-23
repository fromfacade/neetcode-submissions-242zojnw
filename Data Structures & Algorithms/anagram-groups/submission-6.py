class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ang = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            ang[sortedS].append(s)
        
        return list(ang.values())