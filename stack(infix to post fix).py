def infix_to_postfix(infix_expr):
    stack=[]
    postfix_expr=''
    precedence= {'+':1,'-':1,'*':2,'/':2,'^':3}
    for char in infix_expr:
        if char.isalnum():
            postfix_expr += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack[-1]!='(':
                postfix_expr +=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='(' and precedence[char] <=precedence[stack[-1]]:
                postfix_expr +=stack.pop()
            stack.append(char)
    while stack:
        postfix_expr += stack.pop()
    return postfix_expr

infix_expr="AB*+C-F/^"
print(infix_to_postfix(infix_expr))      