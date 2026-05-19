class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for oper in operations:
            if oper == "+":
                record.append(record[-1] + record[-2])
            elif oper == "C":
                record.pop()
            elif oper == "D":
                record.append(2 * record[-1])
            else:
                record.append(int(oper))
        return sum(record)