class Solution:
    def twoSum(self, nums, target):
        storage = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement not in storage:
                storage[num] = index
            else:
                return [storage[complement], index]

x = Solution()
print(x.twoSum([2, 7, 11, 15], 26))
