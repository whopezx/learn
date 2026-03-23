class Solution:
    def removeStars(self, s: str) -> str:
        # ans = ''
        # for si in s:
        #     if si != '*':
        #         ans += si
        #     else:
        #         ans = ans[:-1]
        # return ans

        # 灵茶山艾府题解，这里操作列表比上面我写的操作字符串要快很多
        # python的列表可以作为一个栈，但是字符串应该不是，所以对字符串的操作会慢
        # python的栈还可以使用collections.deque，这是一个双端的栈，首尾都可以入栈出栈，列表只能是在栈顶（列表末端）操作
        st = []
        for c in s:
            if c == '*':
                st.pop()
            else:
                st.append(c)
        return ''.join(st)


if __name__ == "__main__":
    s = Solution()
    print(s.removeStars(s = "leet**cod*e"))