'''
 * กลุ่มที่  : 23010016
 * 65010049 กษิดิ์เดช พุทธวงศ์
 * chapter : 8	item : 2	ครั้งที่ : 0005
 * Assigned : Saturday 16th of September 2023 09:40:20 PM --> Submission : Sunday 17th of September 2023 07:24:56 PM	
 * Elapsed time : 1304 minutes.
 * filename : 2.py
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

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

inp = input("Enter Input : ").split()

inp = list(map(int,inp))

avl = AVL()
root = None

for data in inp:
    print(f"Insert : ( {data} )")
    avl.add(data)
    root = avl.root
    avl.printTree(root)
    print("--------------------------------------------------")
    # print(avl.getHeight(root))