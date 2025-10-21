from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans = 0
        maxans = 0
        # 这里实际上不需要这一步，根据灵茶山艾府的题解，直接从后面开始索引即可
        cardPoints = cardPoints[-k:] + cardPoints[:k]
        for i in range(2*k):
            ans += cardPoints[i]
            if i < k-1:
                continue
            maxans = max(maxans, ans)
            ans -= cardPoints[i-k+1]
        return maxans
        # # 灵茶山艾府题解
        # ans = s = sum(cardPoints[:k])
        # for i in range(1, k + 1):
        #     s += cardPoints[-i] - cardPoints[k - i]
        #     ans = max(ans, s)
        # return ans



if __name__ == '__main__':
    s = Solution()
    print(s.maxScore(cardPoints = [100,40,17,9,73,75], k = 3))