class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        negative = x < 0
        if negative:
            x *= -1
        while x != 0:
            pop = x % 10
            x = x // 10
            reverse = reverse * 10 + pop

        if negative:
            reverse *= -1

        if abs(reverse) > 2**31 - 1:
            return 0
        return reverse

sol = Solution()
print(sol.reverse(-123))
