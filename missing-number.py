class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m = max(nums)
        mn = min(nums)
        for i in range(len(nums)):
            if i not in nums:
                return i
        else:
            return m + 1
