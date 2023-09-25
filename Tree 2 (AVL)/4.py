def nameValue(val):
    sum = 0
    for char in val:
        sum += ord(char)
    return sum

class TreeNode(object):
    def __init__(self, val):
        self.data = val
        self.cdata = nameValue(val)
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return self.data + " (" + str(nameValue(self.data)) + ")"


class AVL_Tree(object):
    def insert(self, root, data):
        cdata = nameValue(data)
        if root is None:
            return TreeNode(data)
        else:
            if cdata < root.cdata:
                root.left = self.insert(root.left,data)
            else:
                root.right = self.insert(root.right,data)

        balance = self.getBalance(root)

        # Left Heavy
        if balance > 1:
            if cdata < root.left.cdata:
                return self.rightRotate(root)
            elif cdata > root.left.cdata:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        # Right Heavy
        if balance < -1:
            if cdata > root.right.cdata:
                return self.leftRotate(root)
            elif cdata < root.right.cdata:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)


        return root 
            

    def delete(self, root, data):
        if root is None:
            return root
        cdata = nameValue(data)
        
        if cdata < root.cdata:  # Compare the first element of data with root.val
            root.left = self.delete(root.left, data)
        elif cdata > root.cdata:  # Compare the first element of data with root.val
            root.right = self.delete(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMinValueNode(root.right)
            root.data = temp.data
            root.cdata = temp.cdata
            root.right = self.delete(root.right, temp.data)

        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balance < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root


    def leftRotate(self, z):
        tempnode = z.right
        z.right = tempnode.left
        tempnode.left = z
        return tempnode

    def rightRotate(self, z):
        tempnode = z.left
        z.left = tempnode.right
        tempnode.right = z
        return tempnode


    def getHeight(self, root):
        if root is None:
            return 0

        if root.left is not None and root.right is not None:
            return max(1 + self.getHeight(root.left),1 + self.getHeight(root.right))
        elif root.left is not None:
            return 1 + self.getHeight(root.left)
        elif root.right is not None:
            return 1 + self.getHeight(root.right)
        else:
            return 1        

    def getBalance(self, root):
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root.left is None:
            return root
        else:
            return self.getMinValueNode(root.left)

    def printTree(self, root, level=0):
        if root is None:
            return
        print("    "*level,end="")
        print(root)
        if root.left or root.right:
            if root.left:
                self.printTree(root.left,level + 1)
            else:
                print("    "*(level + 1),end="")
                print("*")
            if root.right:
                self.printTree(root.right,level + 1)
            else:
                print("    "*(level + 1),end="")
                print("*")
        else:
            return

avl_tree = AVL_Tree()
root = None
inp = input("Enter the data of your friend: ").split(",")
print("------------------------------")
for i in inp:
    op, *data = i.split(" ")
    data = data[0] if data else ""
    # print(data)
    if op == "I":
        root = avl_tree.insert(root, data)
    elif op == "D":
        root = avl_tree.delete(root, data)
    elif op == "P":
        avl_tree.printTree(root)
        print("------------------------------")