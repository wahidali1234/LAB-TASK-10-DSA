class AVLNode:
    def _init_(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def _init_(self):
        self.root = None

    def insert(self, key):
        def _insert(node, key):
            if not node:
                return AVLNode(key)
            elif key < node.key:
                node.left = _insert(node.left, key)
            else:
                node.right = _insert(node.right, key)

            node.height = 1 + max(self._height(node.left), self._height(node.right))
            balance = self._get_balance(node)

            if balance > 1 and key < node.left.key:
                return self._right_rotate(node)
            if balance < -1 and key > node.right.key:
                return self._left_rotate(node)
            if balance > 1 and key > node.left.key:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)
            if balance < -1 and key < node.right.key:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)

            return node

        self.root = _insert(self.root, key)

    def delete(self, key):
        # Implement deletion operation
        pass

    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    def _right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self._height(y.left), self._height(y.right))
        x.height = 1 + max(self._height(x.left), self._height(x.right))

        return x