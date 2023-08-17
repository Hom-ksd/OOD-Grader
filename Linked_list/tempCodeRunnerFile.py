class Node:
    def __init__(self,data,next = None,previous = None):
        self.data = data
        self.next = next
        self.previous = previous
    def __str__(self) -> str:
        return str(self.data)
    
class LinkedList:
    def __init__(self,head = None,tail = None):
        self.head = head 
        self.size = 0
        self.tail = tail

    def isEmpty(self):
        return self.size == 0
    
    def append(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = self.tail = newnode
        else:
            h = self.head
            while h.next != None:
                h = h.next
            h.next = newnode
            newnode.previous = h
            self.tail = newnode
        self.size += 1
                
    def insert_head(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = self.tail = newnode
        else:
            newnode.next = self.head
            self.head = newnode
        self.size += 1

    def insert_between(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head.next
            self.head.next = newnode
        self.size += 1
    
    def max(self):
        h = self.head 
        max_value = 0
        while h != None:
            if abs(h.data) >= max_value:
                max_value = abs(h.data)
            h = h.next
        return max_value
    
    def get_digit(self,n,d):
        n = abs(int(n))
        for i in range(d-1):
            n //= 10
        return n % 10
    
    def get_max_digit(self,n):
        n = abs(n)
        i = 0
        while n >0:
            n //= 10
            i += 1
        return i 
    
    def reverse(self):
        if self.head == None:
            return ""
        else:
            t = self.tail 
            res = ""
            while t != None:
                res += str(t.data) + " "
                t = t.previous
        return res
    
    def str_format(self):
        h = self.head
        res1 = ""
        while h != None:
            res1 += str(h.data) + " -> "
            h = h.next
        return res1[:-3]
    
    def __str__(self) -> str:
        h = self.head 
        res = ""
        while h != None:
            res += str(h.data) + " "
            h = h.next
        return res
    
def join_Link(L1,L2,x):
        L3 = LinkedList()
        if L1.head != None and L2.head != None:
            L1.tail.next = L2.head
            L3.head  = L1.head
            L3.tail = L2.tail
        elif L1.head == None and L2.head != None:
            L3.head = L2.head
            L3.tail = L2.tail
        elif L1.head != None and L2.head == None:
            L3.head = L1.head
            L3.tail = L1.tail
        else:
            return ""
        if x == 0:
            return L3.str_format()
        else:
            return L3
def radix_pos(l_pos):
    max_bits_pos = l_pos.get_max_digit(l_pos.max())
    ll_pos = [LinkedList(),LinkedList(),LinkedList(),LinkedList(),LinkedList(),
        LinkedList(),LinkedList(),LinkedList(),LinkedList(),LinkedList()]
    for i in range(1,(max_bits_pos)+1):
        x = 9
        while l_pos.head != None:
            num_pos = l_pos.head.data
            index_digit = l_pos.get_digit(num_pos,i)
            ll_pos[index_digit].append(num_pos)
            l_pos.head = l_pos.head.next
        l_pos.tail = None
        for j in range(10):
            if ll_pos[j].head != None:
                if l_pos.head == None: 
                    l_pos.head = ll_pos[j].head
                    l_pos.tail = ll_pos[j].tail
                    ll_pos[j].head = ll_pos[j].tail = None
                else:
                    l_pos.tail.next = ll_pos[j].head
                    l_pos.tail = ll_pos[j].tail
                    ll_pos[j].head = ll_pos[j].tail = None
            x -=1
    return l_pos
def radix_neg(l_neg):
    max_bits_neg = l_neg.get_max_digit(l_neg.max())
    ll_neg = [LinkedList(),LinkedList(),LinkedList(),LinkedList(),LinkedList(),
        LinkedList(),LinkedList(),LinkedList(),LinkedList(),LinkedList()]
    
    for i in range(1,(max_bits_neg)+1):
        x = 9
        while l_neg.head != None:
            num_neg = l_neg.head.data
            index_digit = l_neg.get_digit(num_neg,i)
            ll_neg[index_digit].append(num_neg)
            l_neg.head = l_neg.head.next
        l_neg.tail = None
        for j in range(10):
            if ll_neg[x].head != None:
                if l_neg.head == None: 
                    l_neg.head = ll_neg[x].head
                    l_neg.tail = ll_neg[x].tail
                    ll_neg[x].head = ll_neg[x].tail = None
                else:
                    l_neg.tail.next = ll_neg[x].head
                    l_neg.tail = ll_neg[x].tail
                    ll_neg[x].head = ll_neg[x].tail = None
            x-=1
    return l_neg

l = LinkedList()
l_pos = LinkedList()
l_neg = LinkedList()
inp = [l.append(int(i)) for i in input("Enter Input : ").split()]
first_linkedlist = LinkedList()
first_linkedlist.head = l.head
first_linkedlist.tail = l.tail
h = l.head
while h != None:
    i = h.data
    if i >= 0:
        l_pos.append(i)
    else:
        l_neg.append(i)
    h = h.next
max_bits = l.get_max_digit(l.max())
ll = [LinkedList() for i in range(10)]
ll_neg = [LinkedList() for i in range(10)]
ll_pos = [LinkedList() for i in range(10)]
for i in range(1,(max_bits)+1):
    x = 9
    while l.head != None:
        num = l.head.data
        index_digit = l.get_digit(num,i)
        ll[index_digit].append(num)
        if num <0 :
            ll_neg[index_digit].append(num)
        else:
            ll_pos[index_digit].append(num)
        l.head = l.head.next
    l.tail = None
    print("------------------------------------------------------------")
    print("Round :",str(i))
    if i == 1:
        for i in range(10):
            print(f"{i} : {ll_neg[i]}{ll_pos[i]}")
    else:
        for i in range(10):
            print(f"{i} : {ll_neg[i]}{ll_pos[i].reverse()}")

    for j in range(10):
        if ll[x].head != None:
            if l.head == None: 
                l.head = ll[x].head
                l.tail = ll[x].tail
                ll[x].head = ll[x].tail = None
            else:
                l.tail.next = ll[x].head
                l.tail = ll[x].tail
                ll[x].head = ll[x].tail = None
        if ll_neg[j].head != None:
            ll_neg[j].head = ll_neg[j].tail = None
        if ll_pos[x].head != None:
            ll_pos[x].head = ll_pos[x].tail = None
        x -= 1
print("------------------------------------------------------------")
print(str(max_bits),"Time(s)")
print("Before Radix Sort :",first_linkedlist.str_format())
print("After  Radix Sort :",join_Link(radix_neg(l_neg),radix_pos(l_pos),0))