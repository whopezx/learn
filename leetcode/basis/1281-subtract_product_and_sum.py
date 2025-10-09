class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = []
        ans = 1
        while n != 0:
            nums.append(n % 10)
            ans *= nums[-1]
            n //= 10
        return ans - sum(nums)
        # # copy其他人的代码，觉得很精妙
        # product = 1
        # sum_digits = 0
        # for digit in str(n):
        #     num = int(digit)
        #     product *= num
        #     sum_digits += num
        # return product - sum_digits



if __name__ == '__main__':
    s = Solution()
    print(s.subtractProductAndSum(4421))