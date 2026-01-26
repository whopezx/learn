from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = -1
        r = len(letters)
        while l+1 < r:
            m = (l+r)//2
            if ord(letters[m]) <= ord(target):
                l = m
            else:
                r = m
        if r == len(letters):
            return letters[0]
        return letters[r]

if __name__ == "__main__":
    s = Solution()
    print(s.nextGreatestLetter(letters = ['x','x','y','y'], target = 'z'))