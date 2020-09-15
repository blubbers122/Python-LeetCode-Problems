class Solution:
    def singleNumber(self, nums):
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                del seen[num]
        return list(seen.keys())[0]

    def singleNumberXOR(self, nums):
        result = 0
        for i in range(len(nums)):
            result = result ^ nums[i]
        return result

s = Solution()
print(s.singleNumberXOR([4,1,2,1,2]))
