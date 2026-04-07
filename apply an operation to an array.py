class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i + 1]:
                nums[i] = 2 * nums[i]
                nums[i + 1] = 0

        for j in range(len(nums)-1):
            for i in range(j + 1, len(nums)):
                if nums[j] == 0:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums
        