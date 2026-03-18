class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        l=len(word)
        if word.isupper():
           return True
        for i in range(1,l):
            if word[i].isupper():
               return False
        return True
