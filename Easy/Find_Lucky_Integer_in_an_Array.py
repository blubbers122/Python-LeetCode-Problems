class Solution:
    def findLucky(self, arr) -> int:
        storage = {}
        for num in arr:
            if num in storage:
                storage[num] += 1
            else:
                storage[num] = 1
        lucky = -1
        for key, value in storage.items():
            if key == value and key > lucky:
                lucky = key
        return lucky

x = Solution()
print(x.findLucky([2,3,3,3,4]))
