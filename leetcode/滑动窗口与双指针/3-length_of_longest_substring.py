from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # ans = 0
        # start = 0
        # end = 0
        # cnt = defaultdict(int)
        # for i in range(len(s)):
        #     end += 1
        #     cnt[ord(s[i])] += 1
        #     if cnt[ord(s[i])] > 1:
        #         for j in range(start, start+s[start:].index(s[i])+1):
        #             cnt[ord(s[j])] -= 1
        #         start = start+s[start:].index(s[i])+1
        #     if end - start > ans:
        #         ans = end - start
        # return ans

        # 灵茶山艾府题解，和我的解法思想一样，不过代码更简洁
        ans = left = 0
        cnt = defaultdict(int)  # 维护从下标 left 到下标 right 的字符及其出现次数
        for right, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:  # 窗口内有重复字母
                cnt[s[left]] -= 1  # 移除窗口左端点字母
                left += 1  # 缩小窗口
            ans = max(ans, right - left + 1)  # 更新窗口长度最大值
        return ans

        # # 对于这道题将字符转为ascii码然后使用hash表存好像更慢了。
        # ans = left = 0
        # cnt = defaultdict(int)  # 维护从下标 left 到下标 right 的字符及其出现次数
        # for right, c in enumerate(s):
        #     cnt[ord(c)] += 1
        #     while cnt[ord(c)] > 1:  # 窗口内有重复字母
        #         cnt[ord(s[left])] -= 1  # 移除窗口左端点字母
        #         left += 1  # 缩小窗口
        #     ans = max(ans, right - left + 1)  # 更新窗口长度最大值
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring(s = "abcbc"))