class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            total_hours = 0
            k = l + (r - l) // 2
            if k == 0: 
                l = 1
                continue
            for p in piles:
                total_hours += (p + k - 1) // k
            if total_hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
