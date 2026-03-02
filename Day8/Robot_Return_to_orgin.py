class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c1,c2,c3,c4=0,0,0,0
        for ch in moves:
            if ch=='R':
                c1+=1
            elif ch=='L':
                c2+=1
            elif ch=='U':
                c3+=1
            else:
                c4+=1
        return c1==c2 and c3==c4
