class Solution:
    def lessstr(self, string):
        ans = ''
        for s in string:
            if s == "#":
                ans = ans[:-1]
            else:
                ans += s
        return ans

    def backspaceCompare(self, s: str, t: str) -> bool:
        ls = self.lessstr(s)
        lt = self.lessstr(t)
        return ls == lt


if __name__ == "__main__":
    s = Solution()
    print(s.backspaceCompare(s = "", t = "#"))