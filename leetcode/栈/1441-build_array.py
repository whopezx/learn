from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        i = 0
        for t in range(1, target[-1]+1):
            ans.append('Push')
            if t != target[i]:
                ans.append('Pop')
            else:
                i += 1
            # # 根据灵茶山艾府题解，这个判断不需要，因为for循环的范围已经除去数据流大于target的部分了
            # if i == len(target):
            #     break
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.buildArray(target = [1,2], n = 4))