# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        while l+1<n:
            m = (l+n)//2
            if guess(m)==1:
                l = m
            elif guess(m) == -1:
                n = m
            else:
                return m
        return n


if __name__ == "__main__":
    s = Solution()
    print(s.guessNumber(n = 10))