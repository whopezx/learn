class Solution:
    def maxDepth(self, s: str) -> int:
        tans = 0
        ans = 0
        tlist = []
        for si in s:
            if si != '(' and si != ')':
                continue
            if tlist and si == ')' and tlist[-1] == '(':
                tlist.pop()
                tans -= 1
            else:
                tans += 1
                ans = max(tans, ans)
                tlist.append(si)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.maxDepth(s = "(1+(2*3)+((8)/4))+1"))