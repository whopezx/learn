from typing import List
import math

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) > math.ceil(hour):
            return -1
        l = 0
        if hour % 1 == 0:
            r = max(dist)
        else:
            r = max(dist) / (hour % 1)
            r -= r % 0.01
            r = math.ceil(r)
        t = 0
        while l+1 < r:
            m = (l+r)//2
            for d in dist[:-1]:
                t += math.ceil(d / m)
            t += dist[-1]/m
            if t <= hour:
                r = m
            else:
                l = m
            t = 0
        return r


if __name__ == "__main__":
    s = Solution()
    print(s.minSpeedOnTime(dist = [1,1,100000], hour = 2.12))