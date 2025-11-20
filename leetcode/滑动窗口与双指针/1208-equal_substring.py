class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # python 使用ord()函数将字符转为ASCII码
        ans = 0
        left = 0
        cost = 0
        for i in range(len(s)):
            cost += abs(ord(t[i]) - ord(s[i]))
            while cost > maxCost:
                cost -= abs(ord(t[left]) - ord(s[left]))
                left += 1
            ans = max(ans, i - left + 1)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.equalSubstring(s = "krrgw", t = "zjxss", maxCost = 19))