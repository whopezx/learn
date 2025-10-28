from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        # 这种方法重复计算太多了
        ans = []
        for i in range(len(nums)):
            if nums[i] == key:
                ans.append(i)
                for j in range(max(i-k,0), min(i+k+1, len(nums))):
                    ans.append(j)
        return list(set(ans))
        # # copy from 灵茶山艾府
        # last = -inf
        # for i in range(k - 1, -1, -1):
        #     if nums[i] == key:
        #         last = i
        #         break
        #
        # ans = []
        # n = len(nums)
        # for i in range(n):
        #     if i + k < n and nums[i + k] == key:
        #         last = i + k
        #     if last >= i - k:  # key 在窗口中
        #         ans.append(i)
        # return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findKDistantIndices(nums = [2,2,2,2,2], key = 2, k = 2))