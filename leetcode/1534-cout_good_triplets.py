from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    if abs(arr[i]-arr[j]) <= a and abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                        ans += 1
        # # 这种方法是看过题解以及别人的方法抄到的，这样提高了计算的效率
        # for i in range(len(arr)):
        #     for j in range(i+1, len(arr)):
        #         if abs(arr[i]-arr[j]) <= a:
        #             for k in range(j+1, len(arr)):
        #                 if abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
        #                     ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countGoodTriplets(arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3))
