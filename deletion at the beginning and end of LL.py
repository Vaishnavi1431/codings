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
LinkedList = LinkedList()
LinkedList.push(1)
LinkedList.push(2)
LinkedList.push(3)
LinkedList.push(4)
LinkedList.insertAtPos(1,10)
LinkedList.deleteAtStart()
LinkedList.deleteAtEnd()
LinkedList.print()
