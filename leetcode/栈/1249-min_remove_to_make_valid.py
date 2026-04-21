class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # 这道题想了很久，主要就是在考虑如何创建一个新的数组，然后往里填东西，
        # 实际上不需要这样，只需要找到需要删掉的括号的索引即可
        tlist = []
        for idx, si in enumerate(s):
            if 97 <= ord(si) <= 122:
                continue
            if tlist and si == ")" and s[tlist[-1]] == '(':
                tlist.pop()
            elif not tlist and si == ")":
                tlist.append(idx)
                continue
            else:
                tlist.append(idx)
        tlist.reverse()
        for tl in tlist:
            if tl == len(s)-1:
                s = s[:tl]
            else:
                s = s[:tl] + s[tl+1:]
        return s



if __name__ == "__main__":
    s = Solution()
    print(s.minRemoveToMakeValid(s = "))(("))