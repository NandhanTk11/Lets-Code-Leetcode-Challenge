class Solution:
    def interpret(self, command: str) -> str:
        c=""
        i=0
        l=len(command)
        while i<l:
            if command[i]=='G':
                c+='G'
                i+=1
            elif command[i]=='(':
                if command[i+1]==')':
                    c+='o'
                    i+=2
                else:
                    c+='al'
                    i+=4
        return c
