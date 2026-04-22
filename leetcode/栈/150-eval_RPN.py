import math
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tlist = []
        for t in tokens:
            if t == '+':
                tlist[-2] += tlist[-1]
                tlist.pop()
            elif t == '-':
                tlist[-2] -= tlist[-1]
                tlist.pop()
            elif t == '*':
                tlist[-2] *= tlist[-1]
                tlist.pop()
            elif t == '/':
                tlist[-2] = int(tlist[-2] / tlist[-1])
                tlist.pop()
            else:
                tlist.append(int(t))
        return tlist[0]


if __name__ == "__main__":
    s = Solution()
    print(s.evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))