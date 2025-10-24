from typing import List
from collections import defaultdict


class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        throw = 0
        cnt = defaultdict(int)
        for i in range(len(arrivals)):
            if cnt[arrivals[i]] == m:
                arrivals[i] = 0
                throw += 1
            else:
                cnt[arrivals[i]] += 1
            if i < w-1:
                continue
            if arrivals[i-w+1] > 0:
                cnt[arrivals[i-w+1]] -= 1
            # # in 关键字在列表和元组中的时间复杂度是O(n)，效率低，导致时间长
            # if (cnt[arrivals[i-w+1]] > 0) and (i-w+1 not in throw):
            #     cnt[arrivals[i-w+1]] -= 1
        return throw


if __name__ == '__main__':
    s = Solution()
    print(s.minArrivalsToDiscard(arrivals = [1,2,1,3,1], w = 4, m = 2))
# [7,3,9,5,2,] 5
# [3,9,5,2,6,] 5
# [9,5,2,6,10] 5
# [5,2,6,10,9] 5
# [5,2,6,10,9,7] 5
# [5,2,6,10,9,7] 6
# [5,2,6,10,9,7,1] 6
# [2,6,10,9,7,1,3] 6
# [2,6,10,9,7,1,3] 7
# [2,6,10,9,7,1,3] 8
# [6,10,9,7,1,3,4] 8
# [10,9,7,1,3,4,6] 8
# [9,7,1,3,4,6,2] 8
# [7,1,3,4,6,2] 9
# [1,3,4,6,2,8] 9
# [1,3,4,6,2,8] 10
# [3,4,6,2,8] 11
# [4,6,2,8] 12
# [4,6,2,8,7] 12
# [4,6,2,8,7,5] 12
# [6,2,8,7,5] 13