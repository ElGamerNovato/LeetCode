class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        firstCounter=0
        while firstCounter<len(nums):
            limitTwice=0
            for secondCounter in range(-len(nums)+1,1):
                if firstCounter != -secondCounter:
                    if nums[firstCounter] == nums[-secondCounter]:
                        if limitTwice>0:
                            del nums[-secondCounter]
                        else:
                            limitTwice+=1
            firstCounter+=1
