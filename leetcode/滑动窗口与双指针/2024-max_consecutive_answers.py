class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = 0
        left = 0
        T = 0
        F = 0
        for a in answerKey:
            if a == 'T':
                T += 1
            elif a == 'F':
                F += 1
            while T > k and F > k:
                if answerKey[left] == 'T':
                    T -= 1
                elif answerKey[left] == 'F':
                    F -= 1
                left += 1
            ans = max(ans, T + F)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxConsecutiveAnswers(answerKey = "FTFFTFTFTTFTTFTTFFTTFFTTTTTFTTTFTFFTTFFFFFTTTTFTTTTTTTTTFTTFFTTFTFFTTTFFFFFTTTFFTTTTFTFTFFTTFTTTTTTF", k = 32))