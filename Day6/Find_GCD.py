class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        a=nums[0]
        b=nums[len(nums)-1]
        gcd=0
        for i in range(1,min(a,b)+1):
            if a%i==0 and b%i==0:
                gcd=i
        return gcd
