class Solution:
    def reverseParentheses(self, s: str) -> str:
        t = [[]]
        for si in s:
            if si == '(':
                t.append([])
                continue
            elif si == ')':
                t[-1].reverse()
                t[-2].extend(t[-1])
                t.pop()
            else:
                t[-1].append(si)
        return ''.join(t[0])


if __name__ == "__main__":
    s = Solution()
    print(s.reverseParentheses(s = "(u(love)i)"))