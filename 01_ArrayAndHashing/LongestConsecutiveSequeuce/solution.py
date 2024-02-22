class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        numSet = set(nums)
        ans = []
        nowStreak = 1
   
        for num in numSet:
            if num - 1 not in numSet:
                nowNum = num
                nowStreak = 1
                while nowNum + 1 in numSet:
                    nowNum += 1
                    nowStreak += 1
                ans.append(nowStreak)

        return max(ans) if ans else 1