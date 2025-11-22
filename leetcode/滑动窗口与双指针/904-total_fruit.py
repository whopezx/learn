from typing import List
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        left = 0
        cnt = defaultdict(int)
        for i in range(len(fruits)):
            cnt[fruits[i]] += 1
            while len(cnt) > 2:
                cnt[fruits[left]] -= 1
                if cnt[fruits[left]] == 0:
                    del cnt[fruits[left]]
                left += 1
            # 这里每次统计values应该是耗时长了点，
            ans = max(ans, sum(cnt.values()))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.totalFruit(fruits = [0,1,2,2]))