class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=nums
        j=len(nums)
        for i in range(len(nums)):
            j+=1
            ans.append(nums[i])
        return ans
