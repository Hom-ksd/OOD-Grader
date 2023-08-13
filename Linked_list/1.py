
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
        while(currnode.next != None):
            print(currnode,end = "")
            print(" <- ",end="")
            currnode = currnode.next
        print(currnode)
    
    def find_zero(self):
        if self.head == None:
            return
        
        if self.head.data == 0:
            return

        currnode = self.head
        while(currnode.next.data != 0):
            currnode = currnode.next

        zero = currnode.next
        currnode.next = None

        currnode = zero
        while(currnode.next != None):
            currnode = currnode.next

        currnode.next = self.head

        self.head = zero
        return




print(" *** Locomotive ***")
inp = input("Enter Input : ").split()

ll = linked_list()

for i in inp:
    ll.append(int(i))

print("Before : ",end="")
ll.print_list()

ll.find_zero()
print("After : ",end="")
ll.print_list()