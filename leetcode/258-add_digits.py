class Solution:
    def addDigits(self, num: int) -> int:
        ans = 0
        while True:
            ans += num % 10
            num //= 10
            if ans < 10 and num == 0:
                return ans
            elif num != 0:
                continue
            else:
                num = ans
                ans = 0


if __name__ == '__main__':
    s = Solution()
    print(s.addDigits(159))