from typing import List

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        ans = 0
        for w in words[left:right+1]:
            if w[0] in ['a', 'e', 'i', 'o', 'u'] and w[-1] in ['a', 'e', 'i', 'o', 'u']:
                ans += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.vowelStrings(words = ["are","amy","u"], left = 0, right = 2))