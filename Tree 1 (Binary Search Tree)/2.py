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

    def printFormatTree(self):
        BST._printFormatTree(self.root,0)
        print("--------------------------------------------------")
    
    def _printFormatTree(root,depth):
        if root is not None:
            BST._printFormatTree(root.getRight(),depth + 1)
            print(" " + "     " * depth + str(root.data))    
            BST._printFormatTree(root.getLeft(),depth + 1)

    def find_below(self,target):
        global path
        path = []
        BST._find_below(self.root,target)
        return path
        

    def _find_below(root,target):
        if root is not None:
            if root.data >= target:
                BST._find_below(root.getLeft(),target)
            else:
                BST._find_below(root.getLeft(),target)
                path.append(root.data)
                BST._find_below(root.getRight(),target)

        


inp = input("Enter Input : ").split("|")

data = inp[0].split()
target = int(inp[1])

tree = BST()
data = [int(num) for num in data]


for d in data:
    tree.add(d)

tree.printFormatTree()

below = tree.find_below(target)
if below == []:
    print(f"Below {target} : Not have")
else:
    print(f"Below {target} : ",end="")
    print(*below)