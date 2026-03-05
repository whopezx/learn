from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # # 错误，我没做出来
        # if k == 1:
        #     return sum(nums)
        # l = 0
        # r = len(nums)
        # m = []
        # m.append(l)
        # for ik in range(1, k):
        #     m.append(ik * (l + r) // k)
        # m.append(r)
        # sumsub = []
        # for i in range(1, len(m)):
        #     sumsub.append(sum(nums[m[i-1]:m[i]]))
        # lastm = 0
        # maxsub = max(sumsub)
        # while lastm < maxsub:
        #     lastm = maxsub
        #     # # 一次确定子数组和，同时更新。这个方法感觉很难分别0和1的子数组更新l，1和2的子数组更新r时的情况。
        #     # subarraysum.append(sum(nums[:m[0]]))
        #     # for im in m[1:]:
        #     #     subarraysum.append(sum(nums[m[im-1]:m[im]]))
        #     # subarraysum.append(sum(nums[m[-1]:]))
        #
        #     # 顺序更新
        #     for i in range(1, len(m)-1):
        #         m[i] = (m[i-1] + m[i+1]) // 2
        #         if sum(nums[m[i-1]:m[i]]) < sum(nums[m[i]:m[i+1]]):
        #             m[i-1] = m[i]
        #         else:
        #             m[i+1] = m[i]
        #         m[i] = (m[i-1] + m[i+1]) // 2
        #         m[0] = l
        #         m[-1] = r
        #     sumsub = []
        #     for i in range(1, len(m)):
        #         sumsub.append(sum(nums[m[i - 1]:m[i]]))
        #     maxsub = max(sumsub)
        # return maxsub

        # 灵茶山艾府题解
        def check(mx: int) -> bool:
            cnt = 1
            s = 0
            for x in nums:
                if s + x <= mx:
                    s += x
                    continue
                if cnt == k:  # 不能继续划分
                    return False
                cnt += 1  # 新划分一段
                s = x
            return True

        left = max(nums) - 1
        right = sum(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right


if __name__ == "__main__":
    s = Solution()
    print(s.splitArray(nums = [10,20,18,16,30,12,16], k = 3))