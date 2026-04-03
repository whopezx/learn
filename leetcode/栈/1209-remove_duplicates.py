class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # ans = []
        # for si in s:
        #     if len(ans) >= k-1 and ans[-k+1:] == list(si * (k-1)):
        #         for i in range(k-1):
        #             ans.pop()
        #     else:
        #         ans.append(si)
        # return "".join(ans)

        # 这种方法是看了leetcode官方的题解写出来的，这种方法比上面的方法快的多，应该是ans[-k+1:] == list(si * (k-1))非常耗时
        ans = []
        ans_num = []
        for si in s:
            if ans and ans[-1] == si:
                ans_num[-1] += 1
                ans.append(si)
                if ans_num[-1] == k:
                    ans_num.pop()
                    for i in range(k):
                        ans.pop()
            else:
                ans_num.append(1)
                ans.append(si)
        return "".join(ans)


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates(s = "deeedbbcccbdaa", k = 3))