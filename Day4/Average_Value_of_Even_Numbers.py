class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s=0
        l=0
        for i in range(len(nums)):
            if nums[i]%2==0 and nums[i]%3==0:
                s+=nums[i]
                l+=1
        if s!=0:
            return s//l
        else:
            return 0

