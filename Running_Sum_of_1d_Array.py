class Solution:
    def runningSum(self, nums):
        run = 0
        arr = []
        for num in nums:
            run += num
            arr.append(run)
        return arr

s = Solution()
print(s.runningSum([3,1,2,10,1]))
