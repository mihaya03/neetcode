'''
方針
・二分探索で昇順を満たさない箇所を探す
・ただし、両端の要素が最小値の場合を考慮する必要がある
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # case: numsの要素数が1
        if len(nums) == 1:
            return nums[0]
    
        left, right = 0, len(nums) - 1

        # case: rotatating=0
        if nums[right] > nums[0]:
            return nums[0]

        # 二分探索
        # 昇順になっていない箇所を探す
        while right >= left:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]    
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1