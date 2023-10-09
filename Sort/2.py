def insertMinHeap(h, i):
    def parent(pos):
        if pos == 0:
            return 0
        if pos % 2 == 0:
            return (pos - 1) // 2
        else:
            return pos//2
    
    current = i

    while h[current] < h[parent(current)]:
        h[current],h[parent(current)] = h[parent(current)],h[current]
        current = parent(current)

def leftChild(pos):
        return 2 * pos

def rightChild(pos):
        return (2 * pos) + 1

def heapDown(h,pos,last):
    # print(pos,last)
    if (pos * 2 + 2 < last):
        if h[pos] > h[pos * 2 + 1] or h[pos] > h[pos * 2 + 2]:
            if h[pos * 2 + 1] < h[pos * 2 + 2]:
                h[pos],h[pos * 2 + 1] = h[pos * 2 + 1],h[pos]
                heapDown(h,pos * 2 + 1,last)
            else:
                h[pos],h[pos * 2 + 2] = h[pos * 2 + 2],h[pos]
                heapDown(h,pos * 2 + 2,last)
    elif (pos * 2 + 1 < last):
         if h[pos] > h[pos * 2 + 1]:
                h[pos],h[pos * 2 + 1] = h[pos * 2 + 1],h[pos]
                heapDown(h,pos * 2 + 1,last)



def delMin(h, last):
    string = f"deleteMin = {h[0]} FindPlaceFor {h[last]}"
    h[last],h[0] = h[0],h[last]
    heapDown(h,0,last)
    print(string)
    print(*h)

h = []
a = input("Enter list of number: ").split(",")
for i in range(len(a)):
    h.append(int(a[i]))
    insertMinHeap(h, i)
    # print(a[i],h)

print("Heap: ", end="")
print(*h)
print("==== heap sort ====")
for last in range(len(h)-1, 0, -1):
    delMin(h, last)
print("==== Sorting a ====")
h.reverse()
print(*h)