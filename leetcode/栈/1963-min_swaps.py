class Solution:
    def minSwaps(self, s: str) -> int:
        ans = []
        for si in s:
            if ans and si == ']' and ans[-1] == '[':
                ans.pop()
            else:
                ans.append(si)
        return len(ans) // 4 + len(ans) // 2 % 2


if __name__ == "__main__":
    s = Solution()
    print(s.minSwaps(s = "]]][[["))