class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node = node(data)
        if self.head is None:
            self.head =new_node
            return
        temp = self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
    def push(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
    def print(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
LinkedList = LinkedList()
LinkedList.push(1)
LinkedList.push(2)
LinkedList.push(3)
LinkedList.push(4)
LinkedList.print()
