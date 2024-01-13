def diameterOfBinaryTree(root):
    def diameter_helper(node):
        nonlocal diameter
        if not node:
            return 0
        left_height = diameter_helper(node.left)
        right_height = diameter_helper(node.right)
        diameter = max(diameter, left_height + right_height)
        return 1 + max(left_height, right_height)

    diameter = 0
    diameter_helper(root)
    return diameter