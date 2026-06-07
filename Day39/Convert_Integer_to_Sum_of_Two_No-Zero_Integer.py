class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        l=[]
        for i in range(1,n):
            if '0' not in str(i) and '0' not in str(n-i):
                l.append(i)
                l.append(n-i)
                break
        return l
