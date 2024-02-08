class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ans = False
        if len(nums) != len(set(nums)):
            ans = True
        return ans