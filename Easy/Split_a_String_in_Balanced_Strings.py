class Solution:
    def balancedStringSplit(self, s: str) -> int:
        R = 0
        c = 0
        for l in s:
            if l == "R":
                R += 1
            else:
                R -= 1
            if R == 0:
                c += 1
        return c

s = Solution()
print(s.balancedStringSplit("RLRRRLLRLL"))
