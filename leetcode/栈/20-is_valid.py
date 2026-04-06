class Solution:
    def isValid(self, s: str) -> bool:
        # # 看了灵茶山艾府的题解，这个题无需把所有的字符都判断一遍，当右括号与栈的最后一个元素不匹配的时候就可以返回了
        # ans = []
        # for si in s:
        #     if ans and (ord(si)-ord(ans[-1]) == 2 or ord(si)-ord(ans[-1]) == 1):
        #         ans.pop()
        #     else:
        #         ans.append(si)
        # return ans == []

        if len(s) % 2:
            return False
        ans = []
        for si in s:
            if si == '(':
                ans.append(')')
            elif si == '[':
                ans.append(']')
            elif si == '{':
                ans.append('}')
            # ans.pop() 会返回移出的元素，例如ans=[')']，则ans.pop()返回')'
            elif not ans or si != ans.pop():
                return False
        return not ans




if __name__ == "__main__":
    s = Solution()
    print(s.isValid(s = "()))"))