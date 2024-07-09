class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        iteratorForNums2=0
        for emptySpaces in range(m,len(nums1)):
            if n!=0:
                nums1[emptySpaces] = nums2[iteratorForNums2]
                iteratorForNums2+=1
            else:
                break
        nums1.sort()
