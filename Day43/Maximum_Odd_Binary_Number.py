class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c=s.count("1")
        l=["0"]*len(s)
        l[len(s)-1]="1"
        for i in range(c-1):
            l[i]="1"
        return "".join(l)
