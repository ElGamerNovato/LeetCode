class Solution:
    def canJump(self, nums: List[int]) -> bool:
        b=False
        pointer1=len(nums)-1
        flag=pointer1
        if len(nums)>1:
            while pointer1>0:
                pointer2=pointer1-1
                while pointer2>=0:
                    if pointer1-pointer2<=nums[pointer2]:
                        pointer1=pointer2
                        flag=pointer1
                        break
                    elif pointer2==0:
                        break
                    else:
                        pointer2-=1
                if pointer2==0:
                    break
            if flag==0:
                b=True
            else:
                b=False
        else:
            b=True
        return b
