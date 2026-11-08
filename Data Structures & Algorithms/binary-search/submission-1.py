class Solution:
    def search(self, nums: List[int], target: int, offset=0) -> int:
        if len(nums) == 0:
            return -1

        midpoint = len(nums) // 2

        if target > nums[midpoint]:
            l = midpoint + 1
            r = len(nums)
            return self.search(nums[l:r], target, offset + l)

        elif target < nums[midpoint]:
            l = 0
            r = midpoint
            return self.search(nums[l:r], target, offset)

        else:
            return midpoint + offset