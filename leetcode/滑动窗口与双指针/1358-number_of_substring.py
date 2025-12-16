from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        left = 0
        cnt = defaultdict(int)
        for i in range(len(s)):
            cnt[s[i]] += 1
            while len(cnt) == 3:
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0:
                    del cnt[s[left]]
                left += 1
            ans += left
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.numberOfSubstrings(s = "acbbcac"))