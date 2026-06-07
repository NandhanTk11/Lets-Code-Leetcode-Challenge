class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        c=len(arr1)
        for i in range(c):
            low,high=0,len(arr2)-1
            while(low<=high):
                mid=(low+high)//2
                if arr2[mid]==arr1[i]:
                    c-=1
                    break
                elif arr2[mid]<=arr1[i]:
                    if abs(arr1[i]-arr2[mid])<=d:
                        c-=1
                        break
                    low=mid+1
                else:
                    if abs(arr1[i]-arr2[mid])<=d:
                        c-=1
                        break
                    high=mid-1
        return c
