from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        l = 0  # 这里设为0是为了避免（l+r）//2会得到0，进而计算tempk+=c//m是除数是0的情况
        r = min(max(candies), sum(candies) // k) + 1
        while l+1 < r:
            tempk = 0
            m = (l+r)//2
            for c in candies:
                tempk += c//m
            if tempk >= k:
                l = m
            else:
                r = m
        return l  # 这里返回l很关键，

        # # 灵茶山艾府题解
        # def check(low: int) -> bool:
        #     return sum(c // low for c in candies) >= k
        #
        # left, right = 0, min(max(candies), sum(candies) // k) + 1
        # while left + 1 < right:
        #     mid = (left + right) // 2
        #     if check(mid):
        #         left = mid
        #     else:
        #         right = mid
        # return left



if __name__ == "__main__":
    s = Solution()
    print(s.maximumCandies(candies = [4,7,5], k = 4))
    # [1,100] 也可以分给两个小孩各50个