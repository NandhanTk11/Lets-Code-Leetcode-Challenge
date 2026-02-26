class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        mx=0
        for ch in s:
            if ch=='(':
                count+=1
            elif ch==')':
                if count>mx:
                   mx=count
                count-=1
        return mx
            
