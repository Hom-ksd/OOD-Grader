inp = input("Enter width, height, and room: ").split()
width = int(inp[0])
height = int(inp[1])
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
class Queue:
    def __init__(self,List = None):
        if List is None:
            self.items = []
        else:
            self.items = List
    def enQueue(self,value):
        self.items.append(value)

    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

    def isFull(self):
        return len(self.items) > 4

    def __str__(self):
        return "[" + ", ".join(str(x) for x in self.items) + ']'

def is_valid(x, y, width, height):
    return 0 <= x < width and 0 <= y < height

pantee = inp[2].split(',')

pantee2 = []

for i in range(len(pantee)):
    pantee2.append([])
    for char in pantee[i]:
        pantee2[i].append(char)

# print(pantee2)
start_x,start_y = None,None
end_x,end_y = None,None
for i in range(len(pantee2)):
    for j in range(len(pantee2[0])):
        if pantee2[i][j] == "F":
            start_x,start_y = j,i
        elif pantee2[i][j] == "O":
            end_x,end_y = j,i
        

queue = Queue()
show_portal = Queue()
visit = []
found_exit = 0
queue.enQueue((start_x, start_y, []))
show_portal.enQueue([(start_x,start_y)])
while not queue.isEmpty():
    x,y,path=queue.deQueue()
    visit.append((x,y))
    for dx,dy in directions:
        new_x,new_y = x + dx,y + dy
        if new_x == end_x and new_y == end_y:
            print("Found the exit portal.")
            exit()
        if is_valid(new_x, new_y, width, height) and pantee2[new_y][new_x] == "_":
            if (new_x,new_y) not in visit:
                show_portal.enQueue(path+[(new_x,new_y)])
                queue.enQueue((new_x, new_y,path))
                visit.append((new_x, new_y))
    while not show_portal.isEmpty():
        print(show_portal)
        show_portal.deQueue()             

if start_x is None:
    print("Invalid map input.")
# else:
#     print((start_x,start_y))
#     print((end_x,end_y))