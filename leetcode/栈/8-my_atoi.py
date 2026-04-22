class Solution:
    def myAtoi(self, s: str) -> int:
        tlist = []
        for si in s:
            if not tlist and (si == '-' or si == '+'):
                tlist.append(si)
            elif not tlist and si == ' ':
                continue
            elif si.isnumeric():
                tlist.append(si)
            else:
                break
        try:
            ans = int("".join(tlist))
        except:
            return 0
        if ans < -2**31:
            return -2**31
        elif ans > 2**31-1:
            return 2**31-1
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi(s = "-+12"))