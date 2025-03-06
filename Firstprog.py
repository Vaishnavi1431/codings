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
    def print(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
LinkedList = LinkedList()
LinkedList.append(1)
LinkedList.append(2)
LinkedList.append(3)
LinkedList.append(4)
LinkedList.print()
