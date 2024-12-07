class CustomTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def create_custom_tree(level, max_level, values):
    
    if level > max_level:
        return None

    node_value = values[min(level, len(values) - 1)]
    node = CustomTreeNode(node_value)
    
    node.left = create_custom_tree(level + 1, max_level, values)
    node.right = create_custom_tree(level + 1, max_level, values)
    return node

def evaluate_tree(root, target, part):
    results = []

    def traverse(node, current_value, target):
        if node is None:
            return

        if node.left is None and node.right is None:
            if target == current_value:
                results.append(current_value)
            return

        if part == 1:
            traverse(node.left, current_value + node.left.value, target)
            traverse(node.right, current_value * node.right.value, target)
        if part == 2:
            traverse(node.left, current_value + node.left.value, target)
            traverse(node.right, current_value * node.right.value, target)
            traverse(node.left, int(str(current_value) + str(node.left.value)), target)
            traverse(node.right,int(str(current_value) + str(node.right.value)), target)
        
    traverse(root, root.value, target)
    return results


def load_data(filename):
    with open(filename) as f:
        strings = [line.rstrip() for line in f]
    
    values, nodeslists = zip(*[
        (int(line.split(":")[0]), list(map(int, line.split(": ")[1].split(" "))))
        for line in strings
    ])
    return list(values), list(nodeslists)


def advent7(values, nodeslists, part=1):
    sums = 0
    for target,nodes in zip(values, nodeslists):
        max_depth = len(nodes) - 1
        root = create_custom_tree(0, max_depth, nodes)
        result = evaluate_tree(root, target, part)
        if target in result:
            sums+=target

    return sums

FILENAME = "/Users/blackbox/Desktop/advent7"
values, nodeslists = load_data(FILENAME)
print("Part 1:", advent7(values, nodeslists, part=1))
print("Part 2:", advent7(values, nodeslists, part=2))
