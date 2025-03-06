from collections import deque
def evaluate(exp):
    stack=deque()
    for token in exp:
        if(len(token)==1 and  not ord(token)>=48 and ord(token)<=57):
           second=stack.pop()
           first=stack.pop()
           res=eval(str(first)+token+str(second))
           stack.append(res)
        else:
           stack.append(int(token))
    return stack.pop()
exp=["10","6","9","3","+","-11","*","/","*","17","+","5","+"] 
print(evaluate(exp)) 
