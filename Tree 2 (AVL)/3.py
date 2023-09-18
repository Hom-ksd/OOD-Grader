class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self) -> None:
        self.root = None

    def add(self,data):
        self.root = self._add(self.root,data)

    def _add(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data < root.data:
                root.left = self._add(root.left,data)
            else:
                root.right = self._add(root.right,data)
            return root

    def printTree(self):
        self._printTree(self.root,0)

    def _printTree(self, node, level = 0):
        if node != None:
            self._printTree(node.right, level + 1)
            print('     ' * level, node)
            self._printTree(node.left, level + 1)

class AVL:

    def __init__(self) -> None:
        self.root = None

    def add(self,data):
        self.root = self._add(self.root,data)

    def _add(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data < root.data:
                root.left = self._add(root.left,data)
            else:
                root.right = self._add(root.right,data)
    
        Hdiff = self.getDiffHeight(root)

        if Hdiff > 1 and data < root.left.data: # Left Higher than Right and new data < root.left data
            return self.rotateRight(root)
        
        if Hdiff < -1 and data >= root.right.data: # Right Higher than Left and new data > root.right data
            return self.rotateLeft(root)
        
        if Hdiff > 1 and data >= root.left.data: # Left Higher than Right and new data > root.left data
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
        
        if Hdiff < -1 and data < root.right.data: # Right Higher than Left and new data < root.right data
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)
    
        return root

    def rotateLeft(self,root):
        tempnode = root.right
        root.right = tempnode.left
        tempnode.left = root
        return tempnode

    def rotateRight(self,root):
        tempnode = root.left
        root.left = tempnode.right
        tempnode.right = root
        return tempnode
    
    def getHeight(self,root):
        if root == None:
            return 0;

        if root.left is not None and root.right is not None:
            return max(1 + self.getHeight(root.left),1 + self.getHeight(root.right))
        elif root.left is not None:
            return 1 + self.getHeight(root.left)
        elif root.right is not None:
            return 1 + self.getHeight(root.right)
        else:
            return 1
        
    def getDiffHeight(self,root):
        if root is None:
            return 0;

        return self.getHeight(root.left) - self.getHeight(root.right)

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def countNode(self,root):
        if root is None:
            return 0
        
        size = 0
        if root.left:
            size += self.countNode(root.left)
        if root.right:
            size += self.countNode(root.right)
        return size + 1
    
    def getRank(self,target):
        m = self.getMax(self.root)
        if target > m:
            return self.countNode(self.root)
        else:
            return self._getRank(self.root,target)


    def _getRank(self,root,target):
        if root is None:
            return 0

        if root.data < target:
            return self.countNode(root.left) + self._getRank(root.right,target) + 1
        elif root.data == target:
            return self.countNode(root.left) + 1
        else:
            return self._getRank(root.left,target)

    def getMax(self,root):
        if root.right is not None:
            return self.getMax(root.right)
        else:
            return root.data 


inp = input("Enter Input : ").split('/')

datas = list(map(int,inp[0].split()))
target = int(inp[1])

avl = AVL()
bst = BST()
root = None

# print(datas)

for data in datas:
    avl.add(data)
    bst.add(data)


bst.printTree()
print("--------------------------------------------------")
# avl.printTree(avl.root)
# print("-----------------------------------------")
# print(avl.countNode(avl.root.left))
print(f"Rank of {target} :",avl.getRank(target))

