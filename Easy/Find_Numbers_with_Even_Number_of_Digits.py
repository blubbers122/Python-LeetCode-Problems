class Solution:
    def findNumbers(self, nums) -> int:
        evens = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                evens += 1
        return evens

s = Solution()
print(s.findNumbers(nums = [555,901,482,1771]))
