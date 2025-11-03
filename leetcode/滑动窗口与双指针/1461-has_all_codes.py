from collections import defaultdict


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        cnt = defaultdict(int)
        sub = s[:k]
        cnt[sub] += 1
        for i in range(k, len(s)):
            sub = sub+s[i]
            sub = sub[1:]
            cnt[sub] += 1
        if len(cnt) == 2**k:
            return True
        else:
            return False



if __name__ == '__main__':
    s = Solution()
    print(s.hasAllCodes(s = "00110", k = 2))