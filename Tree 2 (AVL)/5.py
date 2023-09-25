class Node:
    def __init__(self, data,id):
        self.data = data
        self.left = None
        self.right = None
        self.id = id
    
    def __str__(self):
        return str(self.data) + ' ' + str(self.id)

class AVL:
    def __init__(self) -> None:
        self.root = None
        self.node_id_counter = 1

    def add(self,data):
        self.root = self._add(self.root,data)
        self.node_id_counter += 1

    def _add(self, root, data):
        if not root:
            return Node(data,self.node_id_counter)

        if data < root.data:
            root.data, data = data, root.data

        if not root.left:
            root.left = self._add(root.left, data)
        elif not root.right:
            root.right = self._add(root.right, data)
        else:
            root.left = self._add(root.left, data)

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

        
    def _heapify_down(self, node):
        if not node:
            return

        smallest = node
        left = node.left
        right = node.right

        if left and (left.data < smallest.data or (left.data == smallest.data and left.id < smallest.id)):
            smallest = left

        if right and (right.data < smallest.data or (right.data == smallest.data and right.id < smallest.id)):
            smallest = right

        if smallest != node:
            node.data, smallest.data = smallest.data, node.data
            node.id, smallest.id = smallest.id, node.id
            self._heapify_down(smallest)



    def addToroot(self,data):
        if self.root is None:
            return
        
        self.root.data += data

    def printCustomer(self,customer,time):
        print(f"Customer {customer} Booking Van {self.root.id} | {time} day(s)")

nums,datas = input("Enter Input : ").split("/")

datas = list(map(int,datas.split()))
nums = int(nums)

avl = AVL()

for i in range(nums):
    avl.add(0)

avl._heapify_down(avl.root)

customer = 1
# avl.printTree(avl.root)
# print("-----------------------------------------------")
for data in datas:
    avl.addToroot(data)
    avl.printCustomer(customer,data)
    customer += 1
    avl._heapify_down(avl.root)
    # avl.printTree(avl.root)
    # print("-----------------------------------------------")
