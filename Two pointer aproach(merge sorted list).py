class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.size=0
    def append(self,data):
        self.size+=1
        new_node = node(data)
        if self.head is None:
            self.head =new_node
            return
        temp = self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
    def push(self,data):
        self.size+=1
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
    def print(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
    def insertAtPos(self,pos,data):
        if pos<1 or pos>self.size+1:
            return
        self.size+=1
        if pos==1:
            self.push(data)
            return
        if pos==self.size+1:
            self.append(data)
            return
        self.size+=1
        newNode = node(data)
        temp=self.head
        i=1
        while(i<pos-1):
            i+=1
            temp=temp.next
        rem=temp.next
        temp.next=newNode
        newNode.next=rem
    def deleteAtStart(self):
        if self.head is None:
            return
        self.head=self.head.next
        self.size+=1
    def deleteAtEnd(self):
        if self.head is None:
            return
        temp=self.head
        while temp.next and temp.next.next:
            temp=temp.next
        temp.next=None
        self.size-=1
    def reverseSLL(self):
        cur=self.head
        left=None
        while(cur):
            right=cur.next
            cur.next=left
            left=cur
            cur=right
        self.head = left
    def merge(self,list2):
        p1=self.head
        p2=list2.head
        res=LinkedList()
        while(p1 and p2):
            if(p1.data<p2.data):
                res.append(p1.data)
                p1=p1.next
            else:
                res.append(p2.data)
                p2=p2.next
        while(p1):
            res.append(p1.data)
            p1=p1.next
        while(p2):
            res.append(p2.data)
            p2=p2.next
        return res
    
list1= LinkedList()
list2= LinkedList()
list1.append(1)
list1.append(3)
list1.append(9)
list1.append(11)
list1.append(13)
list1.append(15)
list2.append(2)
list2.append(4)
list2.append(6)
list2.append(8)
list2.append(10)
res=list1.merge(list2)
res.print()
