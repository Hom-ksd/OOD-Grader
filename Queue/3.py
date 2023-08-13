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
        return "[" + ", ".join("\'" + i + "\'" for i in self.queue) + "]"
        
todo_list = input("input : ").split(",")

def check_string(string):
    return_char = ""
    return_num = 0
    numbers = [1,2,3,4,5,6,7,8,9,0]
    for char in string:
        if char == 'E' or char == 'D':
            return_char = char
        elif return_char != 'E' and return_char != 'D':
            return_char = 'F'

        if not char.isalpha() and int(char) in numbers:
            return_num *= 10
            return_num += int(char)
    
    return return_char,return_num

error_deq = 0
error_inp = 0
start = 0

Q = Queue()

for todo in todo_list:
    char,num = check_string(todo)
    # print(char,num)
    if char == 'E':
        for i in range(num):
            Q.push('*' + str(start))
            start += 1
    elif char == 'D':
        pop_left = num
        while not Q.isEmpty():
            Q.pop()
            pop_left -= 1
        
        if pop_left > 0 :
            error_deq += pop_left
            pop_left = 0

    elif char == 'F':
        error_inp += 1

    print(f"Step : {todo}")
    if char == 'E':
        print(f"Enqueue : {Q}")
    elif char == 'D':
        print(f"Dequeue : {Q}")
    else:
        print(Q)
    print(f"Error Dequeue : {error_deq}")
    print(f"Error input : {error_inp}")
    print("--------------------")
