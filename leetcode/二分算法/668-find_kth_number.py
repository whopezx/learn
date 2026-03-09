class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        l = 0
        r = m*n+1
        while l+1 < r:
            mid = (l+r)//2
            count = 0
            for mi in range(1, m+1):
                count += min(mid // mi, n)
            if count < k:
                l = mid
            else:
                r = mid
        return r


if __name__ == "__main__":
    s = Solution()
    print(s.findKthNumber(m = 3, n = 3, k = 6))