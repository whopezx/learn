class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count('1') < k:
            return ''
        ans = int('1'*len(s))
        left = 0
        sum_s = 0
        for i in range(len(s)):
            sum_s += int(s[i])
            while sum_s > k or s[left]=='0':
                sum_s -= int(s[left])
                left+=1
            if sum_s == k:
                ans = min(int(s[left:i+1]), ans)
        return str(ans)

if __name__ == "__main__":
    s = Solution()
    print(s.shortestBeautifulSubstring(s ="10100010", k = 5))