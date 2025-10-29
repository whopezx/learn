class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        snum = str(num)
        s = ''
        ans = 0
        for i in range(len(snum)):
            s += snum[i]
            if i < k-1:
                continue
            if int(s) is not 0 and num % int(s) == 0:
                ans += 1
            s = s[1:]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.divisorSubstrings(num = 430043, k = 2))