class Solution(object):
    def moveZeroes(self, nums):
        nonzero, i = 0, 0
        n = len(nums)
        while i < n:
            if nums[i] != 0:
                nums[i], nums[nonzero] = nums[nonzero], nums[i]
                nonzero += 1
            i += 1
        
