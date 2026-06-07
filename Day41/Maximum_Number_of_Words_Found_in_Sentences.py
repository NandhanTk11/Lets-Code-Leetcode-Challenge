class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        cmax=0
        for s in sentences:
            c=s.count(" ")+1
            if c>cmax:
                cmax=c
        return cmax
