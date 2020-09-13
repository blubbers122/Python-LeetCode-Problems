class Solution:
    def subtractProductAndSum(self, n):
        product = 1
        sum = 0
        while n != 0:
            digit = n % 10
            product *= digit
            sum += digit
            n = n // 10
        return product - sum

s = Solution()
print(s.subtractProductAndSum(4421))
