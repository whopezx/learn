class Solution:
    def calculate(self, s: str) -> int:
        num = []
        sign = 1
        n = 0
        i = 0
        while i <= len(s)-1:
            if s[i].isdecimal():
                while i <= len(s)-1 and s[i].isdecimal():
                    n = 10 * n + int(s[i])
                    i += 1
                if sign == 2:
                    num[-1] *= n
                elif sign == 3:
                    num[-1] = int(num[-1] / n)
                else:
                    num.append(sign * n)
                n = 0
                continue
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '*':
                sign = 2
            elif s[i] == '/':
                sign = 3
            i += 1
        return sum(num)

        # leetcode官方题解与我的思想是一样的，先乘除后加减，写法优雅很多


if __name__ == "__main__":
    s = Solution()
    print(s.calculate(s = "14-3/2"))