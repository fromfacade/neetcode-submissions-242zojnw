class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset = set()
        for i in nums:
            numset.add(i)
            i+=1
        numset = list(numset)
        print(numset)
        if numset != nums:
            return True
        else:
            return False
