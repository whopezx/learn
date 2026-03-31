class Solution:
    def removeDuplicates(self, s: str) -> str:
        # 昨晚2696之后来做这道题的，思路一样，看完灵茶山艾府题解后很容易了
        ans = []
        for si in s:
            if ans and ans[-1] == si:
                ans.pop()
            else:
                ans.append(si)
        return "".join(ans)


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates("abbaca"))