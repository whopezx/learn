# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n
        while l+1<r:
            m = (l+r)//2
            if isBadVersion(m):
                r = m
            else:
                l = m
        return r


if __name__ == "__main__":
    s = Solution()
    print(s.firstBadVersion(n = 5))