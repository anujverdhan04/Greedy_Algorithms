class Solution:
    def checkValidString(self, s: str) -> bool:

        low = 0
        high=0
        for ch in s:
            if ch=='(' :
                low +=1
                high +=1
            elif ch==')':
                low -=1
                high -=1
            else:
                low -=1 # * consider as ')'
                high +=1 # * consider as '('   

            if high <0:
                return False
            if low <0:
                low =0      
        return low ==0    
        


'''
        count = 0
        n = len(s)   
        for i in range(n):
            if count < 0:
                return False
            if s[i] == ')':
                count -= 1
            elif s[i] == '(' or s[i] == '*':
                count += 1

        return count == 0
            
'''
'''
        st =[]
        n = len(s)
        for i in range(n):
            if(s[i]=='[' or s[i]=='{' or s[i]=='('):
                st.append(s[i])
            else:
                if(len(st) ==0):
                    return False
                ch= st.pop()
                if (s[i] == ')' and ch != '(') or (s[i] == ']' and ch != '[') or (s[i] == '}' and ch != '{'):
                        return False
            return (len(st)==0)            
'''
        