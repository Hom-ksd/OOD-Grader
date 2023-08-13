# Queue
class Queue:
    def __init__(self) -> None:
        self.queue = []

    def enQueue(self,data):
        self.queue.append(data)
    
    def deQueue(self):
        return self.queue.pop(0)

    def frist(self):
        return self.queue[0]
    
    def isEmpty(self):
        if self.queue:
            return False
        self
        return True

# Stack
class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop(-1)
    
    def peek(self):
        return self.stack[-1]
    
    def isEmpty(self):
        if self.stack:
            return  False
        else:
            return True
        

# Linked List        
class node:
    def __init__(self,data,next = None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return str(self.data)

class linked_list:
    def __init__(self,head = None) -> None:
        self.head = head

    def append(self,data):
        data_node = node(data=data)
        if self.head == None :
            self.head = data_node
            return self.head    
        else:
            currnode = self.head
            while currnode.next != None:
                currnode = currnode.next
            currnode.next = data_node

        return self.head

    def del_head(self):
        if self.head == None:
            return None
        
        currnode = self.head
        self.head = currnode.next
        return self.head

    def del_tail(self):
        if self.head == None:
            return None
        
        currnode = self.head
        while currnode.next.next != None:
            currnode = currnode.next
        
        del currnode.next
        return self.head
    
    def add_to_head(self,data):
        newnode = node(data=data)
        newnode = self.head
        self.head = newnode
        return self.head
    
    def add_to_back(self,data):
        newnode = node(data=data)
        if self.head == None:
            self.head = newnode
            return self.head
        
        currnode = self.head
        while currnode.next != None:
            currnode = currnode.next
        
        currnode.next = newnode
        return self.head

    def print_list(self):
        if self.head == None:
            return
        
        currnode = self.head
        while(currnode != None):
            print(currnode,end = "")
            print("->",end="")
            currnode = currnode.next
        print("None")