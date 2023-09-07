class node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self) -> str:
        return str(self.data)

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def append(self,data):
        new_node =  node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return

        currnode = self.tail
        currnode.next = new_node
        new_node.prev = currnode
        self.tail = new_node
        print(self.head,self.tail)

    def addHead(self,data):
        new_node = node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        
        new_node.next = self.head
        self.head = new_node

    def delHead(self):
        if self.head == None:
            return
        
        targetnode = self.head
        self.head = self.head.next
        self.head.prev = None
        del(targetnode)
        if self.head == None:
            self.tail = None

    def delTail(self):
        if self.tail == None:
            return
        
        targetnode = self.tail
        self.tail = targetnode.prev
        self.tail.next = None
        del(targetnode)
        if self.tail == None:
            self.head = None

    def delIndex(self,index):
        if self.head == None:
            return
        
        if index == 0:
            self.delHead()

        elif index + 1 == self.size():
            self.delTail()

        elif index > self.size():
            return
        else:
            print(type(index),index)
            target_index = 0
            currnode = self.head 
            while currnode.next != None:
                if target_index + 1 == index:
                    target_node = currnode.next
                    next_node = target_node.next
                    currnode.next = next_node
                    next_node.prev = currnode
                    del(target_node)
                    return
                currnode = currnode.next
                target_index += 1
    
    def size(self):
        if self.head == None:
            return 0
        
        currnode = self.head
        size = 0
        while currnode != None:
            currnode = currnode.next
            size += 1
        return size
    
    def __str__(self) -> str:
        string = ""
        if self.head == None:
            return string
        
        currnode = self.head
        while(currnode != None):
            string += str(currnode.data) + " "
            currnode = currnode.next
        return string
    