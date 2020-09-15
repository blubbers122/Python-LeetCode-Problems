class Solution():
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

    def reverseString2(self, s):
        for i in range(0, int(len(s)/2)):
            temp = s[i]
            s[i] = s[-1-i]
            s[-1-i] = temp
        return s
        
s = Solution()
print(s.reverseString(["h","e","l","l","o"]))
