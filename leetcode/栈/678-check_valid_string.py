from bisect import bisect_left


class Solution:
    # 我这里比较复杂，先用栈将所有可以不使用*就能匹配的括号剔除，然后创建了三个列表来存储剩余的'(', ')', '*'，
    # 然后使用二分法来进行判断。
    # 实际上看了leetcode官方题解之后只需要创建两个列表来存储'(', '*'即可。具体过程参考leetcode官方题解
    def popl(self, idx_list, star_list):
        for l in idx_list:
            idx = bisect_left(star_list, l)
            if idx == len(star_list):
                return False
            star_list.pop(idx)
        return True

    def popr(self, idx_list, star_list):
        for r in idx_list:
            idx = bisect_left(star_list, r)
            if idx == 0:
                return False
            star_list.pop(idx - 1)
        return True

    def checkValidString(self, s: str) -> bool:
        tlistl = []
        tlistr = []
        tlists = []
        for idx, si in enumerate(s):
            if tlistl and si == ')' and s[tlistl[-1]] == '(':
                tlistl.pop()
            elif si == '*':
                tlists.append(idx)
            elif si == '(':
                tlistl.append(idx)
            elif si == ')':
                tlistr.append(idx)
        if not tlistl and not tlistr:
            return True
        elif tlistl and not tlistr:
            return self.popl(tlistl, tlists)
        elif not tlistl and tlistr:
            return self.popr(tlistr, tlists)
        else:
            return self.popl(tlistl, tlists) and self.popr(tlistr, tlists)


if __name__ == "__main__":
    s = Solution()
    print(s.checkValidString(s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))