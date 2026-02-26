class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
     count=0
     mov=0
     for i in range(len(nums)):
        mov=mov+nums[i]
        if mov==0:
            count+=1
     return count   
