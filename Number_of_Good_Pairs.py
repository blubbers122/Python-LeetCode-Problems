class Solution:
    def numIdenticalPairs(self, nums):
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        pairs = 0
        for _, value in seen.items():
            if value > 1:
                pairs += (value**2 - value) / 2
        return int(pairs)

s = Solution()
print(s.numIdenticalPairs([1,2,3]))
