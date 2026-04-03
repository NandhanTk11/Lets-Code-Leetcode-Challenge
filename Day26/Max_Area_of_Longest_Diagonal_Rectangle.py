class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxd,maxa=0,0
        for l,w in dimensions:
            d=(l*l+w*w)
            a=l*w
            if d>maxd or (d==maxd and a>maxa):
                maxd,maxa=d,a
        return maxa
