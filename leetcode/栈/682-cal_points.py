from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # 简单题，灵茶山艾府没用try，就是单纯的if判断，我这里想试一下try所以写了try
        temp = []
        for ops in operations:
            try:
                temp.append(int(ops))
            except ValueError:
                if ops == "C":
                    temp.pop(-1)
                elif ops == "D":
                    temp.append(temp[-1] * 2)
                else:
                    temp.append(temp[-1]+temp[-2])
        return sum(temp)


if __name__ == "__main__":
    s = Solution()
    print(s.calPoints(operations = ["5","2","C","D","+"]))