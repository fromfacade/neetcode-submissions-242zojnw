class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            ana[sortedS].append(s)

        return list(ana.values())