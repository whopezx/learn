from typing import List
from collections import defaultdict

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        # ans = 0
        # maxans = 0
        # # j = 0  # 子数组长度是否满足长度k
        # sub = []
        # for i in range(len(nums)):
        #     # # 数组中不会有整型以外的元素，题目只是说子数组的定义，实际上大数组是整数数组
        #     # if not isinstance(nums[i], int):
        #     #     ans = 0
        #     #     j = 0
        #     #     continue
        #     sub.append(nums[i])
        #     ans += nums[i]
        #     # # 由于没有其他元素，所以这里也不需要j来反复判断子数组长度
        #     # if j < k-1:
        #     #     j += 1
        #     #     continue
        #     if i < k-1:
        #         continue
        #     # 这里set耗时非常多，所以换成哈希表之后统计长度就不会怎么耗时
        #     if len(set(sub)) >= m:
        #         maxans = max(maxans, ans)
        #     ans -= nums[i-k+1]
        #     sub.pop(0)
        # return maxans

        ans = 0
        maxans = 0
        cnt = defaultdict(int)  # 哈希表，实际上和字典区别不是很大，不过这个字典在没有key的时候添加value自动创建key
        for i in range(len(nums)):
            ans += nums[i]
            cnt[nums[i]] += 1
            if i < k-1:
                continue
            if len(cnt) >= m:
                maxans = max(maxans, ans)
            ans -= nums[i-k+1]
            cnt[nums[i-k+1]] -= 1
            if cnt[nums[i-k+1]] == 0:
                del cnt[nums[i-k+1]]
        return maxans


if __name__ == "__main__":
    s = Solution()
    print(s.maxSum(nums = [1,2,2], m = 2, k = 2))