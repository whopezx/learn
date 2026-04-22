class Solution:
    def minSwaps(self, s: str) -> int:
        ans = []
        for si in s:
            if ans and si == ']' and ans[-1] == '[':
                ans.pop()
            else:
                ans.append(si)
        # 这里这样返回是因为，只有']['这种情况是存在问题的，如测试例子中的移动方式，移动一次可以使两对括号合规
        # 所以如果是偶数的不合规的括号，即']][['，']]]][[[['，分别移动1次，2次即可合规
        # 如果是奇数的不合规的括号，即']['，']]][[['，则需要需要移动1次，2次（1次使两对括号合规，另1次使剩下的1对括号合规）
        return len(ans) // 4 + len(ans) // 2 % 2


if __name__ == "__main__":
    s = Solution()
    print(s.minSwaps(s = "]]][[["))