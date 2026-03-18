class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        s=prices[0]+prices[1]
        if (money-s)<0:
            return money
        else:
            return money-s
