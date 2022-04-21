class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node):
    if not node:
        return []
    ans, level = [], [node]
    while level:
        ans += ([root.value for root in level])
        temp = []
        for root in level:
            temp.append(root.left)
            temp.append(root.right)
        level = [leaf for leaf in temp if leaf]
    return ans


if not tree_by_levels(None):
    print('OK')
else:
    print(tree_by_levels(None))
if tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)) == [1, 2, 3, 4, 5, 6]:
    print('OK')
else:
    print(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)))
