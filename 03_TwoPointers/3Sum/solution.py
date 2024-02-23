from typing import List
class Solution:
    def three_sum(nums):
        nums.sort()  # 配列をソート
        result = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
               continue        
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                      right -= 1
    
        return result