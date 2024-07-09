class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        copyNums=nums
        for counter in range(-1, len(nums)-1):
            nums[counter+1]=copyNums[counter]
            print(copyNums[counter], counter)
