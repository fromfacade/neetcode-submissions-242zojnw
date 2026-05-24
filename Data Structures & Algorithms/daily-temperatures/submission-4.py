class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = []

        for temp in range(n):
            days = 1
            for j in range(temp + 1, n):
                if temperatures[j] > temperatures[temp]:
                    break
                j += 1
                days += 1
            
            if j == n:
                days = 0

            res.append(days)

        res[n - 1] = 0
        return res