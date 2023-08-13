
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
        if self.head == None:
            self.head = newnode
            return
        
        newnode.next = self.head
        self.head = newnode
    
    def pop_head(self):
        if self.head == None:
            return None
        
        delnode = self.head
        self.head = self.head.next
        return delnode.data
    
    def __str__(self) -> str:
        if self.head == None:
            return "None"
        
        return_string = ""
        currnode = self.head
        while currnode.next != None:
            return_string += str(currnode.data) + " "
            currnode = currnode.next
        return_string += str(currnode.data) + " "
        return return_string
        
    def isEmpty(self):
        return self.head == None


l1,l2 = input("Enter Input (L1,L2) : ").split(" ")

ll1 = linked_list()
ll2 = linked_list()

for data in l1.split("->"):
    ll1.append(data)

for data in l2.split("->"):
    ll2.append(data)

print("L1    :",ll1)
print("L2    :",ll2)

temp_ll = linked_list()

while(not ll2.isEmpty()):
    temp_ll.add_to_head(ll2.pop_head())

print("Merge : ",end="")
print(ll1,end="")
print(temp_ll)


