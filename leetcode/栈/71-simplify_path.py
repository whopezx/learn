class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        idx = 0
        path += '/'
        print(path.split('/'))
        for pi, p in enumerate(path):
            if p == '/':
                if path[idx:pi] == '/.':
                    pass
                elif path[idx:pi] == '/..':
                    if ans:
                        ans.pop()
                elif pi-idx > 1:
                    ans.append(path[idx:pi])
                idx = pi
        if not ans:
            return '/'
        return ''.join(ans)

        # # 灵茶山艾府题解，这里主要是字符串的split省时间了，我逐个字符循环，这里分裂完只需要对每个字符串循环
        # stk = []
        # for s in path.split('/'):
        #     if s == "" or s == ".":
        #         continue
        #     if s != "..":
        #         stk.append(s)
        #     elif stk:
        #         stk.pop()
        # return '/' + '/'.join(stk)


if __name__ == "__main__":
    s = Solution()
    print(s.simplifyPath(path = "/.../a/../b/c/../d/./"))