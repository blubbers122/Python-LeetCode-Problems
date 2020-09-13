from collections import Counter

class Solution:
    def firstUniqChar(self, s):
        seen = {}
        for char in s:
            seen[char] = seen.get(char, 0) + 1

        for index, char in enumerate(s):
            if seen[char] == 1:
                return index
        return -1

s = Solution()
print(s.firstUniqChar(s = "loveleetcode"))
