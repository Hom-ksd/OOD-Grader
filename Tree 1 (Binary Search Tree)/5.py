class Queue:
    def __init__(self, q=None):
        if q == None:
            self.item = []
        else:
            self.item = q

    def enQueue(self, i):
        self.item.append(i)

    def deQueue(self):
        return self.item.pop(0)

    def peek(self):
        return self.item[0]

    def isEmpty(self):
        return self.item == []

    def size(self):
        return len(self.item)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def add(self, data):
        self.root = BST._add(self.root, data)

    def _add(root, data):
        if root is None:
            return Node(data)
        else:
            if data < root.data:
                root.left = BST._add(root.left, data)
            else:
                root.right = BST._add(root.right, data)
        return root

    def inOrder(self):
        return BST._inOrder(self.root)

    def _inOrder(node, l=None, level=0):
        if l is None:
            l = []

        if node is None:
            return
        BST._inOrder(node.left, l, level + 1)
        l.append([node.data, level])
        BST._inOrder(node.right, l, level + 1)
        return l

    def levelOrder(self):
        q = Queue()
        q.enQueue([self.root, 0, None])
        l = []
        while not q.isEmpty():
            node, level, parent = q.deQueue()
            l.append([node.data, level, parent])
            if node.left is not None:
                q.enQueue([node.left, level + 1, node])
            if node.right is not None:
                q.enQueue([node.right, level + 1, node])
        return l


inp = [int(i) for i in input("Enter input: ").split()]

tree = BST()
for i in inp:
    tree.add(i)

inOrder = tree.inOrder()
levelOrder = tree.levelOrder()
q = Queue()
for node in levelOrder:
    q.enQueue(node)

level = 0
while not q.isEmpty():
    prevIndex = -1
    edge, line = "", ""
    edgeEnd = -1
    while q.peek()[1] == level:
        node = q.deQueue()
        searchNode = node[:-1]
        index = inOrder.index(searchNode)
        parentIndex = 0

        if node[2] != None:
            parentIndex = inOrder.index([node[2].data, node[1] - 1])

        spaces = " " * len(
            " ".join([str(node[0]) for node in inOrder[prevIndex + 1 : index]])
        )

        if index != 0:
            spaces += " "
        if prevIndex != -1:
            spaces += " "

        if index < parentIndex:
            edgeSpace = ""
            if prevIndex == -1:
                edgeSpace = spaces + " " * len(str(inOrder[index][0]))
            else:
                edgeSpace = " " * len(" ".join([str(node[0]) for node in inOrder[edgeEnd + 1 : index]])) + " " * len(str(inOrder[index][0]))
                edgeSpace += " " * 2
            edge += edgeSpace

            if parentIndex - index > 1:
                edge += "_" * len(" ".join([str(node[0]) for node in inOrder[index + 1 : parentIndex]]))
                edge += "_"
            edge += "/"
            edge += " " * len(str(inOrder[parentIndex][0]))
            edgeEnd = parentIndex

        if index > parentIndex:
            edgeSpace = ""
            if prevIndex == -1:
                edgeSpace = " " * len(" ".join([str(node[0]) for node in inOrder[:parentIndex]]))
                if parentIndex != 0:
                    edgeSpace += " "
                edgeSpace += " " * len(str(inOrder[parentIndex][0]))
            else:
                edgeSpace = " " * len(" ".join([str(node[0]) for node in inOrder[edgeEnd+1:parentIndex]]))
                if parentIndex - edgeEnd > 1:
                    edgeSpace += " " * 2
                    edgeSpace += " " * len(str(inOrder[parentIndex][0]))

            edge += edgeSpace
            edge += "\\"

            if index - parentIndex > 1:
                edge += "_" * len(" ".join([str(node[0]) for node in inOrder[parentIndex + 1 : index]]))
                edge += "_"

            edge += " " * len(str(inOrder[index][0]))
            edgeEnd = index

        line += spaces
        line += str(node[0])
        prevIndex = index

        if q.isEmpty():
            break

    if node[2] != None:
        print(edge)
    print(line)
    level += 1