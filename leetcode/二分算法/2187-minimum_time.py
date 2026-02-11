from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l = 0
        r = min(time) * totalTrips  # 这里使用min(time)就可以无需使用max(time)，因为最小的耗时跑totalTripes就能完成要求的数目
        n_trip = 0
        while l+1 < r:
            m = (l+r)//2
            for t in time:
                n_trip += m//t
            if n_trip < totalTrips:
                l = m
            else:
                r = m
            n_trip = 0
        return r


if __name__ == "__main__":
    s = Solution()
    print(s.minimumTime(time = [1,2,3], totalTrips = 5))