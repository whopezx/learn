class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = blocks[:k].count("W")
        min_ans = ans
        # if ans == 0:  # 前k的元素就正好都是黑色的概率是很低的，所以不进行判断，减少耗时
        #     return 0
        for i in range(k, len(blocks)):
            if min_ans == 0:
                return 0
            if blocks[i] == "W" and blocks[i-k] == "B":
                ans += 1
            elif blocks[i] == "B" and blocks[i-k] == "W":
                ans -= 1
            if ans < min_ans:
                min_ans = ans
        return min_ans
        # # 灵茶山艾府题解，没使用判断，因为机器执行判断时会预测执行哪个分支，预测错误会回滚之前的指令重新执行降低计算速度
        # ans = cnt_w = blocks[:k].count('W')
        # for in_, out in zip(blocks[k:], blocks):
        #     cnt_w += (in_ == 'W') - (out == 'W')
        #     ans = min(ans, cnt_w)
        # return ans



if __name__ == '__main__':
    s = Solution()
    print(s.minimumRecolors(blocks = "WBBWWWWBBWWBBBBWWBBWWBBBWWBBBWWWBWBWW", k = 15))