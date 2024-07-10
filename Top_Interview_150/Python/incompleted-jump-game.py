class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        b=False
        i=0
        while i < len(nums):
            maxNum=-1
            maxPos=0
            for j in range(i+1, i+1+nums[i]):
                if nums[j]>maxNum:
                    maxNum=nums[j]
                    maxPos=j
            i=maxPos
            if i+nums[i]>=len(nums):
                b=True
                break
            if i==0:
                break
        return b
