class Solution:
    def getEatingSpeed(self, k, piles):
        total = 0
        for pile in piles:
            total += math.ceil(pile/k)
        return total

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            k = (l + r) // 2
            eatingSpeed = self.getEatingSpeed(k, piles)
            if eatingSpeed > h:
                l = k+1
            else:
                r = k-1
        return l