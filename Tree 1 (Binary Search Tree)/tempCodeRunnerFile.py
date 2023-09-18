class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def vertical_tree(root, level, result):
    if root is None:
        return
    if level not in result:
        result[level] = []
    result[level].append(root.value)
    vertical_tree(root.left, level - 1, result)
    vertical_tree(root.right, level + 1, result)

def print_vertical_tree(root):
    result = {}
    vertical_tree(root, 0, result)
    
    min_level = min(result.keys())
    max_level = max(result.keys())
    
    for level in range(min_level, max_level + 1):
        if level in result:
            values = result[level]
            max_width = 5  # Width of each node value (adjust as needed)
            print(" " * (level - min_level) * max_width, end="")
            for value in values:
                value_str = f"{value:^{max_width}}"
                if level < max_level:
                    print(value_str[:-1] + "/", end="")
                elif level > min_level:
                    print("_" * (max_width - 1) + " ", end="")
                else:
                    print(value_str, end="")
            print()

if __name__ == "__main__":
    input_data = [-100, -120, -110, -110, -130, -90, -60, -70, -75, -74, -76]
    root = None
    for value in input_data:
        root = insert(root, value)
    
    # Adjust the tree for printing
    root.left.right = TreeNode(-90)
    root.left.right.right = TreeNode(-110)
    root.right = TreeNode(-60)
    root.right.left = TreeNode(-70)
    root.right.left.right = TreeNode(-75)
    root.right.left.right.left = TreeNode(-76)
    root.right.left.right.right = TreeNode(-74)
    
    print_vertical_tree(root)
