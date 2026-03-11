class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        h=-1
        s=0
        n=x
        while(x>0):
            s+=x%10
            x//=10
        return h if n%s!=0 else s
