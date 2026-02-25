class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2==0:
            return n
        else:
            n*=2
            if n%2==0:
                return n
