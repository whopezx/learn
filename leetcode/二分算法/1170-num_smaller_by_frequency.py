from typing import List


class Solution:
    def bisect(self, nums, target):
        l = -1
        r = len(nums)
        while l+1 < r:
            m = (l+r)//2
            if nums[m] <= target:
                l = m
            else:
                r = m
        return r

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        ans = []
        for i in range(len(words)):
            # # 参考灵茶山艾府评论，这里只是统计数目，无需使用二分查找
            # temp = sorted(words[i])
            # words[i] = self.bisect(temp, temp[0])
            words[i] = words[i].count(min(words[i]))
        words.sort()
        for q in queries:
            # # 和上面一样，无需使用二分查找
            # q = sorted(q)
            # nq = self.bisect(q, q[0])
            nq = q.count(min(q))
            ans.append(len(words) - self.bisect(words, nq))
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.numSmallerByFrequency(queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]))