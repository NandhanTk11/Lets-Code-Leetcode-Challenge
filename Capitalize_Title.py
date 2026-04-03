class Solution:
    def capitalizeTitle(self, title: str) -> str:
        l=title.split()
        r=[]
        for word in l:
            if len(word)>2:
                word=word.capitalize()
            else:
                word=word.lower()
            r.append(word)
        return " ".join(r)
