class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            part = target - num
            if part in nums:
                j = nums.index(part)
                if i != j:
                    return sorted([i, j])
        return