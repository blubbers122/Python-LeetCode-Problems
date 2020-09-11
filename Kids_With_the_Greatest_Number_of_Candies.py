class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        return [candy + extraCandies >= max(candies) for candy in candies]
x = Solution()
print(x.kidsWithCandies([2,3,5,1,3], 1))
