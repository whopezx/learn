class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = start
        for i in range(1,n):
            result = result ^ (start+2*i)
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.xorOperation(5,0))