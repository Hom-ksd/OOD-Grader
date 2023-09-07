def deleteIsland(Map,y,x):
    if (y < 0 or y >= len(Map)) or (x >= len(Map[y]) or x < 0):
        return
    
    if Map[y][x] == 0:
        return
    
    if Map[y][x] == 1:
        Map[y][x] = 0

    direction = [(0,-1),(1,0),(0,1),(-1,0)]

    for dx,dy in direction:
        deleteIsland(Map,y + dy,x + dx)
    

def countIsland(Map):
    count = 0
    for i in range(len(Map)):
        for j in range(len(Map[i])):
            if Map[i][j] == 1:
                count += 1
                deleteIsland(Map,i,j)
    return count

Input = input("Enter Input : ").split('/')

Map=[]

for i in Input:

    temp=[*i]

    temp = list(map(int,temp))

    Map.append(temp)

print(f"Island have : {countIsland(Map)}")

