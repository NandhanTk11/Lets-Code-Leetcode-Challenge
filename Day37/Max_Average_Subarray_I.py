class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxs=sum(nums[:k])
        s=maxs
        for i in range(k,len(nums)):
            s+=nums[i]-nums[i-k]
            if s>maxs:
                maxs=s
        return maxs/k
