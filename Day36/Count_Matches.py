class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        r={"type":0,"color":1,"name":2}
        count=0
        i=r[ruleKey]
        for item in items:
            if ruleValue==item[i]:
                count+=1
        return count
