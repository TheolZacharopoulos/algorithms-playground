from data_structures.binary_trees.bst_operations.BST import BSTNode


def find_node_recursive(root, value):
    if root is None:
        return None

    node_value = root.get_data()

    if node_value == value:
        return root
    elif node_value < value:
        return find_node_recursive(root.get_right(), value)
    else:
        return find_node_recursive(root.get_left(), value)


def find_node_iteratively(root, value):
    while root is not None:
        node_value = root.get_data()

        if node_value == value:
            break
        elif node_value < value:
            root = root.get_right()
        else:
            root = root.get_left()

    return root


r = BSTNode(5,
            BSTNode(3,
                    BSTNode(2),
                    BSTNode(4)),

            BSTNode(7,
                    BSTNode(6),
                    BSTNode(8)))

print(find_node_recursive(r, 6))
print(find_node_iteratively(r, 6))
print(find_node_recursive(r, 3))
print(find_node_iteratively(r, 3))

print(find_node_recursive(r, 9))
print(find_node_iteratively(r, 9))