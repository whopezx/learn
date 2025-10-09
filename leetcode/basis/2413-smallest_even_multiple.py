class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2==0:
            return n
        else:
            return 2*n

if __name__ == '__main__':
    s = Solution()
    print(s.smallestEvenMultiple(n=3))