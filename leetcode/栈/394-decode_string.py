class Solution:
    def decodeString(self, s: str) -> str:
        numlist = []
        letterlist = ['']
        idxbegin = None
        for idx, si in enumerate(s):
            # 这里判断si是否是数字的情况有三个函数，isdigit(), isnumeric(), isdecimal()
            if si.isdecimal() and idxbegin is None:
                idxbegin = idx
            elif si.isalpha():
                letterlist[-1] += si
            elif si == '[':
                # 这里'['前肯定是有数字的所以无需担心idxbegin没有值
                numlist.append(int(s[idxbegin:idx]))
                idxbegin = None
                letterlist.append('')
            elif si == ']':
                letterlist[-2] += numlist[-1] * letterlist[-1]
                letterlist.pop()
                numlist.pop()
        return letterlist[0]


if __name__ == "__main__":
    s = Solution()
    print(s.decodeString(s = "100[leetcode]"))