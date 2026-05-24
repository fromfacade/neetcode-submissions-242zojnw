class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = []

        for i in range(n):
            days = 1
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    break
                j += 1
                days += 1
            
            if j == n:
                days = 0

            res.append(days)

        res[n - 1] = 0
        return res