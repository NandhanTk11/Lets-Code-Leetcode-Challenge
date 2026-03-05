class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=0
        p=1
        while n>0:
            t=n%10
            p=p*t
            s+=t
            n=n//10
        return p-s
