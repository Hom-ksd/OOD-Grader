class Node:
    def __init__(self, data,parent = None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent
        self.isBurn = False

    def __str__(self):
        return str(self.data)

class AVL:

    def __init__(self) -> None:
        self.root = None
        self.mtime = 0

    def add(self,data):
        self.root = self._add(self.root,data,None)

    def _add(self, root, data, parent):
        if root is None:
            return Node(data,parent)
        else:
            if data < root.data:
                root.left = self._add(root.left,data,root)
            else:
                root.right = self._add(root.right,data,root)
    
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
        if tempnode.left:
            tempnode.left.parent = root
        tempnode.parent = root.parent
        root.parent = tempnode
        tempnode.left = root
        return tempnode

    def rotateRight(self,root):
        tempnode = root.left
        root.left = tempnode.right
        if tempnode.right:
            tempnode.right.parent = root
        tempnode.parent = root.parent
        root.parent = tempnode
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
            print('     ' * level, node, node.parent)
            self.printTree(node.left, level + 1)

    def findData(self,data):
        return self._findData(self.root,data)

    def _findData(self,root,data):
        # print(root)
        if root is None:
            return None

        if root.data == data:
            return root
        else:
            if root.left and root.right:
                left = self._findData(root.left,data)
                right = self._findData(root.right,data)
                if left != None :
                    return left
                elif right != None:
                    return right
                else:
                    return None
            elif root.left:
                return self._findData(root.left,data)
            elif root.right:
                return self._findData(root.right,data)

    def burning(self,root):
        queue = []
        visited = set()
        time = 0
        queue.append((time,[root]))
        while queue:
            # print(queue)
            target_node = queue.pop(0)
            print(" ".join(str(node) for node in target_node[1]))

            lst = []
            for node in target_node[1]:
                # print(node)
                node.isBurn = True
                if node not in visited:
                    if node.left and node.left not in visited:
                        lst.append(node.left)
                    if node.right and node.right not in visited:
                        lst.append(node.right)
                    if node.parent and node.parent not in visited:
                        lst.append(node.parent)
                    visited.add(node)
            # print(visited)
            if lst != []:
                time += 1
                queue.append((time,lst.copy()))

datas,target = input("Enter node and burn node : ").split('/')

datas = list(map(int,datas.split()))
target = int(target)

avl = AVL()
root = None

for data in datas:
    avl.add(data)
    root = avl.root

# avl.printTree(avl.root)

node_target = avl.findData(target)

if node_target is not None:
    ans = avl.burning(node_target)
else:
    print(f"There is no {target} in the tree.")

