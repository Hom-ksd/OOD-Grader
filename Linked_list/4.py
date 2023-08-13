
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
    
    def set_next(self,start,end):
        if self.head == None:
            return "Error! {list is empty}"
        
        pos = 0
        currnode = self.head

        firstNode = None
        secondNode = None

        while currnode != None:
            if pos == int(start):
                firstNode = currnode
            if pos == int(end):
                secondNode = currnode

            pos += 1
            currnode = currnode.next

        if firstNode == None:
            return "Error! {index not in length}: " + str(start)

        if secondNode == None:
            self.append(end)
            return "index not in length, append : " + str(end)

        firstNode.next = secondNode
        return f"Set node.next complete!, index:value = {start}:{firstNode.data} -> {end}:{secondNode.data}"
    
    def check_loop(self):
        if self.head == None:
            return False,"No Loop"
        
        startnode = self.head
        currnode = self.head
        
        if startnode.next == startnode:
            return True,"Found Loop"

        while startnode.next != None:
            visit = []
            while currnode.next != None and currnode not in visit:
                visit.append(currnode)
                if currnode.next in visit:
                    return True,"Found Loop"
                currnode = currnode.next
            startnode = startnode.next
        
        return False,"No Loop"


    def size(self) -> int:
        if self.haed == None:
            return 0
        
        cnt = 1
        currnode = self.head
        while currnode.nexdt != None:
            cnt += 1
            currnode = currnode.next

        return cnt

    def __str__(self) -> str:
        if self.head == None:
            return "Empty"
        
        return_string = ""
        currnode = self.head
        visit = []
        while currnode.next != None and currnode not in visit:
            visit.append(currnode)
            return_string += str(currnode.data) + "->"
            currnode = currnode.next
        return_string += str(currnode.data)
        return return_string
        
    def isEmpty(self):
        return self.head == None
    
inp = input("Enter input : ").split(",")
ll= linked_list()


for i in inp:
    if i[0] == 'A':
        ll.append(i[2:])
        print(ll)
    elif i[0] == 'S':
        st,ed = i[2:].split(":")
        print(ll.set_next(st,ed))
isFound,toPrint = ll.check_loop()
if not isFound:
    print(toPrint)
    print(ll)
else:
    print(toPrint)