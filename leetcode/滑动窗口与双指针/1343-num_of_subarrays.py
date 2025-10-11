from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        sum_arr = sum(arr[:k])
        threshold = threshold * k
        if sum_arr >= threshold:
            ans += 1
        for i in range(k, len(arr)):
            sum_arr = sum_arr - arr[i-k] + arr[i]
            if sum_arr >= threshold:
                ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numOfSubarrays(arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5))