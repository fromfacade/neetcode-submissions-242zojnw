class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:        
        for i in range(len(arr)):
            j = i + 1
            m = 0
            for j in range(i+1, len(arr)):
                if arr[j] > m:
                    m = arr[j]
            arr[i] = m

        arr[len(arr) - 1] = -1

        return arr
            

