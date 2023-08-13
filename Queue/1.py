class Queue:
    def __init__(self):
        self.queue = []

    def push(self,data):
        self.queue.append(data)

    def pop(self):
        return self.queue.pop(0)

    def front(self):
        return self.queue[0]
    
    def size(self):
        return len(self.queue)

    def isEmpty(self):
        if self.queue:
            return False
        else:
            return True
        
    def __str__(self):
        return "[" + ", ".join('\'' + str(i) + '\'' for i in self.queue) + "]"
    
Q = Queue()
inp = input("Enter Input : ").split(",")

for todo in inp:
    if todo == 'D':
        if Q.isEmpty():
            print("-1")
        else:
            print(f"Pop {Q.pop()} size in queue is {Q.size()}")
    else:
        action = todo.split(" ")[0]
        data = todo.split(" ")[1]
        Q.push(data)
        print(f"Add {data} index is {Q.size() - 1}")

if Q.isEmpty():
    print("Empty")
else:
    print(f"Number in Queue is :  {Q}")