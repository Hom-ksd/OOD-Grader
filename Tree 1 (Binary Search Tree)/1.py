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
    
    def find_path(self):
        global path
        path = []
        BST._find_path(self.root,0)
        return path

    def _find_path(root,depth):
        if root is None:
            return
        
        if root.getLeft() is None and root.getRight() is None:
            path.append(depth)
            return 
        
        if root.getLeft() and root.getRight():
            BST._find_path(root.getLeft(),depth + 1)
            BST._find_path(root.getRight(),depth + 1)
        elif root.getLeft():
            BST._find_path(root.getLeft(),depth + 1)
        elif root.getRight():
            BST._find_path(root.getRight(),depth + 1)

        
inp = input("Enter input: ").split()
tree = BST()
for data in inp:
    tree.add(int(data))

allPath = tree.find_path()
print(f"{len(allPath)} path(s)")
if allPath != []:
    for i in range(max(allPath),0,-1):
        if i in allPath:
            print(f"{allPath.count(i)} path(s) that pass through {i} node(s)")
