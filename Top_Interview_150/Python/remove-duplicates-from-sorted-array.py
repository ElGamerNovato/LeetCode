class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        firstCounter=0
        while firstCounter < len(nums):
            secondCounter = len(nums)-1
            while secondCounter >= 0:
                if firstCounter != secondCounter:
                    if nums[firstCounter] == nums[secondCounter]:
                        del nums[secondCounter]
                secondCounter-=1
            firstCounter+=1
