class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        se=sum(nums)
        sb=0
        for n in nums:
            while n>0:
                t=n%10
                sb+=t
                n=n//10
        return se-sb
