from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        cnt = defaultdict(int)
        for i in range(len(s)):
            cnt[s[i]] += 1
            while cnt[s[i]] > 2:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, sum(cnt.values()))  # 这里计算cnt中value的和会慢
            # ans = max(ans, i - left + 1)  # 参考灵茶山艾府题解，这里使用这种方式会快一些
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maximumLengthSubstring(s = "abcbbcb"))
    # abcbbcb