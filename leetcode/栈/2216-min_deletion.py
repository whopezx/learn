from typing import List


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        ans = 0
        temp_n = []
        for n in nums:
            if len(temp_n)%2 and temp_n[-1] == n:
                ans+=1
            else:
                temp_n.append(n)
        if len(temp_n)%2 == 0:
            return ans
        else:
            return ans + 1


if __name__ == "__main__":
    s = Solution()
    print(s.minDeletion(nums = [1,1,2,2,3,3]))