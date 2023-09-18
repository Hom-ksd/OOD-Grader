class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class MinHeap:
    def __init__(self):
        self.root = None

    def push(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if node.left is None:
            node.left = TreeNode(value)
            self._heapify_up(node.left)
        elif node.right is None:
            node.right = TreeNode(value)
            self._heapify_up(node.right)
        else:
            if self._count_nodes(node.left) <= self._count_nodes(node.right):
                self._insert(node.left, value)
            else:
                self._insert(node.right, value)

    def pop(self):
        if self.root is None:
            return None

        min_value = self.root.value

        last_node = self._get_last_node()
        if last_node is not self.root:
            self.root.value = last_node.value
            self._delete_last_node(last_node)

        self._heapify_down(self.root)

        return min_value

    def _get_last_node(self):
        last_node = None
        queue = [self.root]

        while queue:
            last_node = queue.pop(0)
            if last_node.left:
                queue.append(last_node.left)
            if last_node.right:
                queue.append(last_node.right)

        return last_node

    def _delete_last_node(self, node_to_delete):
        queue = [self.root]

        while queue:
            current_node = queue.pop(0)
            if current_node.left is node_to_delete:
                current_node.left = None
                break
            elif current_node.right is node_to_delete:
                current_node.right = None
                break
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    def _heapify_up(self, node):
        if node is None or node == self.root:
            return

        parent = self._find_parent(self.root, node)
        if parent and node.value < parent.value:
            node.value, parent.value = parent.value, node.value
            self._heapify_up(parent)

    def _find_parent(self, root, node):
        if root is None:
            return None
        if (root.left is node) or (root.right is node):
            return root
        left_parent = self._find_parent(root.left, node)
        if left_parent:
            return left_parent
        return self._find_parent(root.right, node)

    def _heapify_down(self, node):
        if node is None:
            return

        smallest = node
        if (node.left is not None) and (node.left.value < smallest.value):
            smallest = node.left
        if (node.right is not None) and (node.right.value < smallest.value):
            smallest = node.right

        if smallest != node:
            node.value, smallest.value = smallest.value, node.value
            self._heapify_down(smallest)

    def _count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

# Example usage:
min_heap = MinHeap()
elements = [4, 2, 9, 7, 5, 1, 8, 3, 6]

for element in elements:
    min_heap.push(element)

while True:
    min_element = min_heap.pop()
    if min_element is None:
        break
    print(min_element, end=" ")
