class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for temp in range(len(temperatures)):
            days = 1
    
            for j in range(temp + 1, len(temperatures)):
                if temperatures[j] > temperatures[temp]:
                    break
                j += 1
                days += 1
            
            if j == len(temperatures):
                days = 0

            res.append(days)

        res[len(temperatures) - 1] = 0
        return res