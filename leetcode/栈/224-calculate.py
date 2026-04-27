class Solution:
    def calculate(self, s: str) -> int:
        # 我的方法，有点慢
        tlist = [0]
        sign = [1]
        num = 0
        for idx, si in enumerate(s):
            if si.isdecimal():
                num = num * 10 + sign[-1] * int(si)
                if idx == len(s)-1 or not s[idx+1].isdecimal():
                    tlist[-1] += num
                    num = 0
                    sign[-1] = 1
            elif si == '(':
                tlist.append(0)
                sign.append(1)
            elif si == ')':
                sign.pop()
                tlist[-2] += sign[-1] * tlist[-1]
                sign[-1] = 1
                tlist.pop()
            elif si == '+':
                sign[-1] *= 1
            elif si == '-':
                sign[-1] *= -1
        return tlist[-1]

        # leetcode官方题解思路：
        # 由于只有加减法，所以可以将括号去掉，然后改变每个数之前的正负号


if __name__ == "__main__":
    s = Solution()
    print(s.calculate(s = "(7)-(0)+(4)"))