class Solution:
    def shuffle(self, nums, n):
        new = []
        for i in range(n):
            new.append(nums[i])
            new.append(nums[n + i])
        return new

s = Solution()
print(s.shuffle([1,2,3,4,4,3,2,1], 4))
