
# Linked List        
class node:
    def __init__(self,data,next = None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return str(self.data)

class linked_list:
    def __init__(self,data,head = None) -> None:
        self.head = head
        self.number = data

    def append(self,data):
        data_node = node(data=data)
        if self.head == None :
            self.head = data_node
        else:
            currnode = self.head
            while currnode.next != None:
                currnode = currnode.next
            currnode.next = data_node

    def addHead(self,data):
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

    def pop_back(self):
        if self.head == None:
            return None
        
        if self.head.next == None:
            node = self.head
            self.head = None
            return node.data

        prevnode = None        
        currnode = self.head
        while currnode.next != None:
            prevnode = currnode
            currnode = currnode.next
        if prevnode != None:
            prevnode.next = None
        return currnode.data
    
    def __str__(self) -> str:
        return_string = ""
        return_string += str(self.number) + " : "
        if self.head == None:
            return return_string
        
        currnode = self.head
        while currnode.next != None:
            return_string += str(currnode.data) + " "
            currnode = currnode.next
        return_string += str(currnode.data) + " "
        return return_string
        
    def isEmpty(self):
        return self.head == None
    
    def print_radix(self):
        return_string = "Radix Sort :"
        currnode = self.head
        while currnode.next != None:
            return_string += " " + str(currnode.data) + " ->"
            currnode = currnode.next
        return_string += " " + str(currnode.data)
        return return_string
    
    def front(self):
        if self.head == None:
            return None
        else:
            return self.head.data
        
    def insert(self,data):
        newnode = node(data)
        if self.head == None:
            self.head = newnode
        
        elif self.head.data <= data:
            self.addHead(data)
        
        else:
            prevnode = None
            currnode = self.head
            while currnode.next != None:
                if currnode.data <= data:
                    prevnode.next = newnode
                    newnode.next = currnode
                    return
                prevnode = currnode
                currnode = currnode.next
            self.append(data)

def get_digits(num,d):
    for i in range(d-1):
        num //= 10
    return num % 10

inp = input("Enter Input : ").split()
before = linked_list("B")
result = linked_list("R")
mx = 0
for i in inp:
    i = int(i)
    result.insert(i)
    before.append(i)
    if i < 0:
        i = -i
    if mx < i:
        mx = i

digits = 0
while(mx > 0):
    digits += 1
    mx = int(mx / 10)

round = 1
# print(digits)


digit_list = [linked_list(0),linked_list(1),linked_list(2),linked_list(3),
              linked_list(4),linked_list(5),linked_list(6),linked_list(7),
              linked_list(8),linked_list(9)]

print("------------------------------------------------------------")
for i in range(1,digits + 1):
    # print(result)
    print(f"Round : {i}")
    while not result.isEmpty():
        data = result.pop_head()
        if data < 0:
            data_digit = get_digits(-data,i)
            # digit_list[data_digit].append(data)
        else:
            data_digit = get_digits(data,i)
            # digit_list[data_digit].addHead(data)
        digit_list[data_digit].append(data)
    for j in digit_list:
        print(j)
    for i in range(9,-1,-1):
        while not digit_list[i].isEmpty():
            data = digit_list[i].front()
            if data < 0:
                break
            digit_list[i].pop_head()
            result.append(data)

    for i in range(10):
        while not digit_list[i].isEmpty():
            data = digit_list[i].pop_head()
            result.append(data)
    print("------------------------------------------------------------")

print(f"{digits} Time(s)")
print("Before ",end="")
print(before.print_radix())
print("After  ",end="")
print(result.print_radix())
