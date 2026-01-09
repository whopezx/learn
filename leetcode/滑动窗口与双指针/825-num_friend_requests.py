from typing import List
from collections import defaultdict

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        ans = 0
        left = 0
        cnt = defaultdict(int)
        for i in range(0, len(ages)):
            if ages[i]>=15:
                cnt[ages[i]] += 1
            while ages[left]<=(0.5*ages[i]+7) and left<i:
                left += 1
            ans += i-left
        for n in cnt.values():
            ans += n*(n-1)//2
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.numFriendRequests(ages = [73,106,39,6,26,15,30,100,71,35,46,112,6,60,110]))