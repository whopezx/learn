class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        tlist = []
        for si in s:
            if tlist and si == ")" and tlist[-1] == '(':
                tlist.pop()
            else:
                tlist.append(si)
        return len(tlist)


if __name__ == "__main__":
    s = Solution()
    print(s.minAddToMakeValid(s = "()))(("))