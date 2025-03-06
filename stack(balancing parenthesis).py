from collections import deque
def isBalanced(s):
    stack=deque()
    for ch in s:
        if (ch=='('or ch=='[' or ch=='{'):
            stack.append(ch)
            continue
        if(len(stack)==0):
            return False
        if(ch=='}'):
            if (stack[-1]=='[' or stack[-1]=='('):
                return False
        if(ch==')'):
             if (stack[-1]=='[' or stack[-1]=='{'):
                return False
        if(ch==']'):     
             if (stack[-1]=='{' or stack[-1]=='('):
                return False
        stack.pop()
    return len(stack)==0
s=input()
print(isBalanced(s))

