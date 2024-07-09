class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for position in range(-len(nums)+1, 1):
            if nums[-position]==val:
                del nums[-position]
        return len(nums)
