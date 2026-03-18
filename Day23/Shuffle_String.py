class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n=len(s)
        st=['']*n
        for i in range(0,n):
            st[indices[i]]=s[i]
        return ''.join(st)
