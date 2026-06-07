class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            ls,rs=0,0
            if i!=len(nums)-1:
                rs=sum(nums[i+1:])
            if i!=0:
                ls=sum(nums[:i])
            ans.append(abs(rs-ls))
        return ans
