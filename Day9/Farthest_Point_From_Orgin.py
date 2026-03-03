class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        c1,c2,c3=0,0,0
        c1=moves.count('L')
        c2=moves.count('R')
        c3=moves.count('_')
        return abs(c1-c2)+c3
