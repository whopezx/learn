class Solution:
    def clumsy(self, n: int) -> int:
        tlist = []
        for idx, i in enumerate(range(n, 0, -1)):
            if idx % 4 == 0:
                tlist.append(i)
            elif idx % 4 == 1:
                tlist[-1] *= i
            elif idx % 4 == 2:
                tlist[-1] //= i
            elif idx % 4 == 3:
                tlist[0] += i
        else:
            if len(tlist) > 1:
                for t in tlist[1:]:
                    tlist[0] -= t
        return tlist[0]


if __name__ == "__main__":
    s = Solution()
    print(s.clumsy(10))