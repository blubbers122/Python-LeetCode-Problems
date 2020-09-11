class Solution:
    def restoreString(self, s, indices):
        new = list(s)
        for count, index in enumerate(indices):
            new[index] = s[count]

        return "".join(new)

s = Solution()
print(s.restoreString(s = "aaiougrt", indices = [4,0,2,6,7,3,1,5]))
