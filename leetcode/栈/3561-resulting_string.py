class Solution:
    def resultingString(self, s: str) -> str:
        # ans = []
        # for si in s:
        #     if ans and (abs(ord(si)-ord(ans[-1])) == 1 or abs(ord(si)-ord(ans[-1])) == 25):
        #         ans.pop()
        #     else:
        #         ans.append(si)
        # return ''.join(ans)

        ans = []
        for si in s:
            if ans and abs(ord(si) - ord(ans[-1])) == 1:
                ans.pop()
            # 这个判断没有用，正常字母相差25就是相邻的，但是这样的写法相比于只有上面一个判断会快
            elif ans and ((si == 'z' and ans[-1] == 'a') or (si == 'a' and ans[-1] == 'z')):
                ans.pop()
            else:
                ans.append(si)
        return ''.join(ans)

        # 这道题灵茶山艾府给出了两个题解，第二个是构建了一个字典，对s循环，进字典里面查找


if __name__ == "__main__":
    s = Solution()
    print(s.resultingString(s = "abc"))