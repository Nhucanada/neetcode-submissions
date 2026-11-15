class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target:
            return 0
        elif len(nums) == 1:
            return -1
        midpoint = len(nums) // 2
        if target > nums[midpoint]:
            l = midpoint
            r = len(nums)
        elif target < nums[midpoint]:
            l = 0
            r = midpoint
        else:
            return midpoint

        return self.search(nums[l:r], target)