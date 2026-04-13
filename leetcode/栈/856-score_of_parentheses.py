class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = 0
        i = 0
        tlist = []
        while i < len(s):
            if s[i] == '(':
                tlist.append(s[i])
                i += 1
                continue
            j = len(tlist)
            while i < len(s) and s[i] == ")":
                i += 1
                tlist.pop()
            ans += 2**(j-1)
        return ans

        # # 力扣官方题解，这个方法不是对括号进行入栈出栈操作，而是对分数进行操作，
        # # 如果是左括号则入栈一个0分，如果是右括号则出栈一个0分，然后剩余栈内最后一个元素加1，这样解决了嵌套括号的问题
        # st = [0]
        # for c in s:
        #     if c == '(':
        #         st.append(0)
        #     else:
        #         v = st.pop()
        #         st[-1] += max(2 * v, 1)
        # return st[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.scoreOfParentheses("(())"))