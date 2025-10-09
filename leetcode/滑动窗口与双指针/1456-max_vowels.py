class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # # 这个方法超过了leetcode的时间上限
        # ans = 0
        # maxans = 0
        # i = 0
        # while i <= len(s)-k:
        #     for si in s[i:i+k]:
        #         if si in 'aeiou':
        #             ans += 1
        #         if ans == k:
        #             return k
        #     if ans > maxans:
        #         maxans = ans
        #     if ans == 0 and i+k <= len(s)-k:
        #         i+=k
        #     else:
        #         ans = 0
        #         i += 1
        # return maxans

        # 参考灵茶山艾府题解，我自己的写法
        ans = 0
        maxans = 0
        for i in range(k):
            if s[i] in 'aeiou':
                ans += 1
                maxans += 1
        for i in range(k, len(s)):
            if s[i] in 'aeiou' and s[i-k] in 'aeiou':  # 这个判断可以删掉
                pass
            elif s[i] in 'aeiou' and s[i-k] not in 'aeiou':
                ans += 1
            elif s[i] not in 'aeiou' and s[i-k] in 'aeiou':
                ans -= 1
            if maxans < ans:
                maxans = ans
        return maxans



if __name__ == '__main__':
    s = Solution()
    print(s.maxVowels(s = "a", k = 1))