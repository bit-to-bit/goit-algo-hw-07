import random

DELIMITER = "\n" + "-" * 80 + "\n"


class AVLNode:

    GAP = "|      "
    ICO_ROOT = "\U0001F331"
    ICO_LEFT = "\U00002570\U00002500\U00002500\U0001F7E1"
    ICO_RIGHT = "\U0000256D\U00002500\U00002500\U0001F7E0"

    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

    def __str__(self, level=0, prefix=ICO_ROOT):
        ret = ""

        if self.right:
            ret += self.right.__str__(level + 1, self.ICO_RIGHT)
        ret += self.GAP * level + prefix + " " + str(self.key) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, self.ICO_LEFT)

        return ret


def get_height(node):
    if not node:
        return 0
    return node.height


def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)


def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y


def right_rotate(y):
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x


def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def insert(root, key):
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root


def delete_node(root, key):
    if not root:
        return root

    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete_node(root.right, temp.key)

    if root is None:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if get_balance(root.left) >= 0:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if get_balance(root.right) <= 0:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root


def generate_random_tree(number_of_nodes: int):
    """Generate random tree"""
    root = None
    random.seed(42)
    keys = random.sample(range(1, (abs(number_of_nodes) + 1) * 2), number_of_nodes)

    for key in keys:
        root = insert(root, key)
    return root


def get_min_key(root: AVLNode):
    """Min key in the tree"""
    min_key = None
    if root:
        current = root
        min_key = current.key
        while current.left is not None:
            current = current.left
            min_key = min(min_key, current.key)
    return min_key


def get_max_key(root: AVLNode):
    """Max key in the tree"""
    max_key = None
    if root:
        current = root
        max_key = current.key
        while current.right is not None:
            current = current.right
            max_key = max(max_key, current.key)
    return max_key


def get_sum_keys(node: AVLNode):
    """Sum all keys in the tree"""
    sum_keys = None
    if node:
        sum_keys = node.key
        if node.right:
            sum_keys += get_sum_keys(node.right)
        if node.left:
            sum_keys += get_sum_keys(node.left)
    return sum_keys


def get_tree_info(root: AVLNode):
    """Return tree info"""
    res = DELIMITER
    res += "\nGenerated tree vizualization:\n"
    res += DELIMITER + "\n"
    res += str(root)
    res += DELIMITER
    res += "\nGenerated tree properties: \n"
    res += "\nMin tree key = " + str(get_min_key(root))
    res += "\nMax tree key = " + str(get_max_key(root))
    res += "\nSum tree key = " + str(get_sum_keys(root))
    res += DELIMITER
    return res
