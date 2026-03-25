from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        l = []
        j = 0
        for i in pushed:
            l.append(i)
            # # 这里while循环可以进一步简化以提高执行效率
            # while l[-1] == popped[j]:
            #     l.pop()
            #     j += 1
            #     if l == []:
            #         break

            while l and l[-1] == popped[j]:
                l.pop()
                j += 1
        return l == []


if __name__ == "__main__":
    s = Solution()
    print(s.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,5,3,2,1]))