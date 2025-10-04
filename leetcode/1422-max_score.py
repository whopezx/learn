class Solution:
    def maxScore(self, s: str) -> int:
        score = len(s)//2-1
        for i in range(1,len(s)):
            score_new = s[:i].count('0') + s[i:].count('1')
            if score_new > score:
                score = score_new
        return score


if __name__ == '__main__':
    s = Solution()
    print(s.maxScore("10"))