from collections import deque
class MyQueue(object):
    def __init__(self):
        self.s1=deque()
        self.s2=deque()
    def push(self,x):
        self.s1.append(x)
    def pop(self):
        if not self.s2:
           while self.s1:
               self.s2.append(self.s1.pop())
        return self.s2.pop()
    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
                return self.s2[-1]
    def empty(self):
        return len(self.s1)==0 and len(self.s2)==0
    
obj=MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())
print(obj.empty())
