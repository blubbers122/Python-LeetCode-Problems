from itertools import count

class Solution:
    def numberOfSteps (self, num: int) -> int:
        for step in count():
            if not num:
                return step
            num = num - 1 if num & 1 else num >> 1


x = Solution()
print(x.numberOfSteps(47))
