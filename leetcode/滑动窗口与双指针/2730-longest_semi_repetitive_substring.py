class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        ans = 1
        left = 1
        repeat = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                repeat += 1
            while repeat > 1:
                if s[left] == s[left - 1]:
                    repeat -= 1
                left += 1
            ans = max(ans, i - (left-1) + 1)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.longestSemiRepetitiveSubstring(s = "2233123"))