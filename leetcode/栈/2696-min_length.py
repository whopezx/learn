class Solution:
    def minLength(self, s: str) -> int:
        # 这种写法根本没有用到栈的思想
        s = list(s)
        i = 1
        while i < len(s):
            if s[i] == 'B' and s[i-1] == 'A':
                s.pop(i)
                s.pop(i - 1)
                i = max(1, i-1)
            elif s[i] == 'D' and s[i-1] == 'C':
                s.pop(i)
                s.pop(i - 1)
                i = max(1, i-1)
            else:
                i += 1
        return len(s)

        # # 参考灵茶山艾府题解，新入栈的元素如果是B并且栈顶是A，则删除栈顶元素，CD同理
        # st = []
        # for c in s:
        #     if st and (c == 'B' and st[-1] == 'A' or c == 'D' and st[-1] == 'C'):
        #         st.pop()
        #     else:
        #         st.append(c)
        # return len(st)


if __name__ == "__main__":
    s = Solution()
    print(s.minLength(s = "ABAB"))