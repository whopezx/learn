class Solution:
    def isValid(self, s: str) -> bool:
        temp_s = []
        for si in s:
            if len(temp_s) >= 2 and si == 'c' and temp_s[-1] == 'b' and temp_s[-2] == 'a':
                temp_s.pop()
                temp_s.pop()
            else:
                temp_s.append(si)
        return temp_s == []


if __name__ == "__main__":
    s = Solution()
    print(s.isValid(s = "aabcbc"))