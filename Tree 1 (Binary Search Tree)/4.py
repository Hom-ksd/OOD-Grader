class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.data)
    
    def getLeft(self) -> str:
        return self.left if self.left != None else None
    
    def getRight(self) -> str:
        return self.right if self.right != None else None
    
class Queue:
    def __init__(self) -> None:
        self.data = []
    
    def enQueue(self,data):
        self.data.append(data)

    def deQueue(self):
        return self.data.pop(0)
    
    def isEmpty(self):
        return len(self.data) == 0
    

class BST:
    def __init__(self) -> None:
        self.root = None

    def add(self,data):
        self.root = BST._add(self.root,data)

    def _add(root, data):
        if root is None:
            return Node(data)
        else:
            if data < root.data:
                root.left = BST._add(root.left,data)
            else:
                root.right = BST._add(root.right,data)
        return root
    
    def preOrder(self):
        BST._preOrder(self.root)
        print()

    def _preOrder(root):
        if root is not None:
            print(root.data,end=" ")
            BST._preOrder(root.getLeft())
            BST._preOrder(root.getRight())

    def inOrder(self):
        BST._inOrder(self.root)
        print()

    def _inOrder(root):
        if root is not None:
            BST._inOrder(root.getLeft())
            print(root.data,end=" ")
            BST._inOrder(root.getRight())

    def postOrder(self):
        BST._postOrder(self.root)
        print()

    def _postOrder(root):
        if root is not None:
            BST._postOrder(root.getLeft())
            BST._postOrder(root.getRight())
            print(root.data,end=" ")

    def BFS(self):
        if self.root is None:
            return None
        queue = Queue()
        queue.enQueue(self.root)
        while not queue.isEmpty():
            target = queue.deQueue()
            left = target.getLeft()
            right = target.getRight()
            if left is not None:
                queue.enQueue(left)
            if right is not None:
                queue.enQueue(right)
            print(target.data,end=" ")
    

inp = input("Enter Input : ").split()
data = list(map(int,inp))
# print(data)
tree = BST()
for d in data:
    tree.add(d)

print("Preorder : ",end="")
tree.preOrder()
print("Inorder : ",end="")
tree.inOrder()
print("Postorder : ",end="")
tree.postOrder()
print("Breadth : ",end="")
tree.BFS()
