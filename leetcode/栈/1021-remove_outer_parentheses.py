class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # ans = [[]]
        # tlist = []
        # ai = 0
        # for si in s:
        #     if tlist and ord(tlist[-1]) == ord(si)-1:
        #         tlist.pop()
        #         ans[ai].append(si)
        #         if not tlist:
        #             ans.append([])
        #             ai += 1
        #     else:
        #         tlist.append(si)
        #         ans[ai].append(si)
        # result = ""
        # for ansi in ans:
        #     result += "".join(ansi[1:-1])
        # return result

        tlist = []
        ans = []
        idx0 = 1
        for idx, si in enumerate(s):
            if tlist and ord(si)-1 == ord(tlist[-1]):
                tlist.pop()
                if not tlist:
                    ans.append(s[idx0:idx])
                    idx0 = idx+2
            else:
                tlist.append(si)
        return "".join(ans)




if __name__ == "__main__":
    s = Solution()
    print(s.removeOuterParentheses(s = "(()())(())"))