# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class node:
    def __init__(self, value=None):
        self.value=value
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def insert(self, value):
        if self.root==None:
            self.root=node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left == None:
                cur_node.left = node(value)
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right == None:
                cur_node.right = node(value)
            else:
                self._insert(value, cur_node.right)
        else:
            print("Value already in tree")

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left)
            print(str(cur_node.value))
            self._print_tree(cur_node.right)

bst = BST()
bst.insert(4)
bst.insert(7)
bst.insert(1)
bst.insert(8)
bst.insert(5)
#bst.print_tree()


class Solution:
    def rangeSumBST(self, root, L, R):
        def dfs(node):
            if node:
                if L <= node.value <= R:
                    self.sum += node.value
                if L < node.value:
                    dfs(node.left)
                if R > node.value:
                    dfs(node.right)
        self.sum = 0
        dfs(root)
        return self.sum
s = Solution()
print(s.rangeSumBST(bst.root, 4, 7))
