class Solution:
    def calculateScore(self, s: str) -> int:
        ans = 0
        L = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        for si in range(len(s)):
            # 25-(ord(s[si])-97) = 122-ord(s[si])
            if L[122-ord(s[si])]:
                ans += si - L[122-ord(s[si])][-1]
                L[122-ord(s[si])].pop()
            else:
                L[ord(s[si])-97].append(si)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.calculateScore(s = "eockppxdqclkhjgvnw"))