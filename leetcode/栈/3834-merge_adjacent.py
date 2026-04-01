from typing import List


class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            while ans and n == ans[-1]:
                ans.pop()
                n += n
            else:
                ans.append(n)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.mergeAdjacent(nums = [2,1,1,2]))