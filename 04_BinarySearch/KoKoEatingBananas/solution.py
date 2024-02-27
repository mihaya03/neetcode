'''
方針
・最小の速さと最大の速さの間で二分探索を行う
'''

from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left <= right:
            mid = left + (right - left) // 2 # オーバーフローを防ぐ
            result = sum(ceil(pile / mid) for pile in piles)
            if result <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left
        