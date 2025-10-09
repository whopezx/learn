class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if 3**19 % n == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPowerOfThree(45))