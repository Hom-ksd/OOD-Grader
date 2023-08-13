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
        return "[" + ", ".join(str(i) for i in self.queue) + "]"
    
width,height,rooms = input("Enter width, height, and room: ").split()
rooms = rooms.split(",")
width = int(width)
height = int(height)
room_map = []
start_pos = (-1,-1)
is_ans = False

if len(rooms) != height:
    print("Invalid map input.")
    is_ans = True
else:
    for iroom in range(len(rooms)):
        temp_room = []
        if len(rooms[iroom]) != width:
            if not is_ans:
                print("Invalid map input.")
                is_ans = True
            break
        else:
            for ichar in range(len(rooms[iroom])):
                temp_room.append(rooms[iroom][ichar])
                if rooms[iroom][ichar] == 'F':
                    start_pos = (ichar,iroom)
        room_map.append(temp_room)

# print map
# for i in range(len(room_map)):
#     for j in range(len(room_map[i])):
#         print(room_map[i][j],end="")
#     print()

if start_pos == (-1,-1) and not is_ans:
    print("Invalid map input.")
    is_ans = True

walk = Queue()
visited = [start_pos]
walk.push(start_pos)

# print(walk)

# N :  0 -1
# E : +1  0
# S :  0 +1
# W : -1  0

while(not is_ans):
    if walk.isEmpty():
        print("Cannot reach the exit portal.")
        break
    print(f"Queue: {walk}") 
    
    if walk.front()[1] - 1 >= 0: # N
        next_pos = (walk.front()[0],walk.front()[1] - 1)
        if room_map[walk.front()[1] - 1][walk.front()[0]] == '_' and next_pos not in visited :
            walk.push((walk.front()[0],walk.front()[1] - 1))
            visited.append((walk.front()[0],walk.front()[1] - 1))
        elif room_map[walk.front()[1] - 1][walk.front()[0]] == 'O':
            print("Found the exit portal.")
            break

    if walk.front()[0] + 1 < width: # E
        next_pos = (walk.front()[0] + 1,walk.front()[1])
        if room_map[walk.front()[1]][walk.front()[0] + 1] == '_' and next_pos not in visited:
            walk.push((walk.front()[0] + 1,walk.front()[1]))
            visited.append((walk.front()[0] + 1,walk.front()[1]))
        elif room_map[walk.front()[1]][walk.front()[0] + 1] == 'O':
            print("Found the exit portal.")
            break
    
    if walk.front()[1] + 1 < height: # S
        next_pos = (walk.front()[0],walk.front()[1] + 1)
        if room_map[walk.front()[1] + 1][walk.front()[0]] == '_' and next_pos not in visited:
            walk.push((walk.front()[0],walk.front()[1] + 1))
            visited.append((walk.front()[0],walk.front()[1] + 1))
        elif room_map[walk.front()[1] + 1][walk.front()[0]] == 'O':
            print("Found the exit portal.")
            break
    
    if walk.front()[0] - 1 >= 0: # W
        next_pos = (walk.front()[0] - 1,walk.front()[1])
        if room_map[walk.front()[1]][walk.front()[0] - 1] == '_' and next_pos not in visited:
            walk.push((walk.front()[0] - 1,walk.front()[1]))
            visited.append((walk.front()[0] - 1,walk.front()[1]))
        elif room_map[walk.front()[1]][walk.front()[0] - 1] == 'O':
            print("Found the exit portal.")
            break
    # print(f" v : {visited}")
    walk.pop()
