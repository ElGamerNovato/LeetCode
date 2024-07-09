class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority=0
        numsNotRepeated = list(dict.fromkeys(nums))
        print(numsNotRepeated)
        for numberToCount in numsNotRepeated:
            counter = 0
            for iterator in range(len(nums)):
                if nums[iterator] == numberToCount:
                    counter+=1
            if counter > len(nums)/2:
                majority = numberToCount
                break
        return majority
