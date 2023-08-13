class Queue:
    def __init__(self,msize):
        self.queue = []
        self.maxsize = msize

    def push(self,data):
        self.queue.append(data)

    def pop(self):
        return self.queue.pop(0)

    def front(self):
        return self.queue[0]
    
    def size(self):
        return len(self.queue)
    
    def maxSize(self):
        if self.maxsize >= 0:
            return self.maxsize

    def isEmpty(self):
        if self.queue:
            return False
        else:
            return True
        
string,n = input("Enter people and time : ").split(" ")
n = int(n)
waiting = Queue(len(string))
cashier1 = Queue(5)
cashier2 = Queue(5)

minute = 1

timer1 = 3
timer2 = 2

for char in string :
    waiting.push(char)

for i in range(n):
    # print(timer1,timer2)
    if timer1 == 0 and not cashier1.isEmpty():
        cashier1.pop()
        if not cashier1.isEmpty():
            timer1 = 3
    if timer2 == 0 and not cashier2.isEmpty():
        cashier2.pop()
        if not cashier2.isEmpty():
            timer2 = 2

    if cashier1.size() < cashier1.maxSize():
        if cashier1.isEmpty():
            timer1 = 3
        if waiting.size() > 0:
            cashier1.push(waiting.pop())
        
    elif cashier2.size() < cashier2.maxSize():
        if cashier2.isEmpty():
            timer2 = 2
        if waiting.size() > 0:
            cashier2.push(waiting.pop())

    timer1 -= 1
    timer2 -= 1     
    
    print(i + 1,waiting.queue,cashier1.queue,cashier2.queue)
