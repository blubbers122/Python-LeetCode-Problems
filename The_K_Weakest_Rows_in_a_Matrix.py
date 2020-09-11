class Solution(object):
    def kWeakestRows(self, mat, k):
        numSoldiers = [(arr.count(1), index) for index, arr in enumerate(mat)]

        numSoldiers = sorted(numSoldiers)
        weakest = []
        for i in range(k):
            soldiers, index = numSoldiers[i]
            weakest.append(index)

        return weakest



x = Solution()
print(x.kWeakestRows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 3))
