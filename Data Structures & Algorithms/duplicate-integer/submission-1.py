class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset = set()
        for i in nums:
            numset.add(i)
            i+=1
        numset = list(numset)
        print(numset)
        if numset != nums:
            print('true')
            return True
        else:
            print('false')
            return False
