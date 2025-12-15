class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans = 0
        left = 0
        num0 = 0
        num1 = 0
        for i in range(len(s)):
            if s[i] == '0':
                num0 += 1
            else:
                num1 += 1
            while num0 > k and num1 > k and left < i:
                if s[left] == '0':
                    num0 -= 1
                else:
                    num1 -= 1
                left += 1
            ans += i-left+1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.countKConstraintSubstrings(s = "10101", k = 1))