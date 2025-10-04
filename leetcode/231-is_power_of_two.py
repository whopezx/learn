class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if bin(n)[2:].count('1') == 1:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfTwo(-16))