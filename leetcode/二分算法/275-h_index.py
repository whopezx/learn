from typing import List
from bisect import bisect_right


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = -1  # citations中有0，如果citations中全是0，则应该返回0
        r = len(citations)  # 对应citations中所有值都很大的情况
        while l+1 < r:
            m = (l+r) // 2
            idx = bisect_right(citations, m)  # 这里用right是为了和下一行len(citations)匹配
            if m < len(citations) - idx:
                l = m
            else:
                r = m
        return r


if __name__ == "__main__":
    s = Solution()
    print(s.hIndex(citations = [1,2,100]))