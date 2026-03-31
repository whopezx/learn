class Solution:
    def makeGood(self, s: str) -> str:
        # 昨晚2696题之后，这道题很容易了
        ans = []
        for si in s:
            if ans and (ord(si) == ord(ans[-1])-32 or ord(si) == ord(ans[-1])+32):
                ans.pop()
            else:
                ans.append(si)
        return "".join(ans)


if __name__ == "__main__":
    s = Solution()
    print(s.makeGood(s = "leEeetcode"))