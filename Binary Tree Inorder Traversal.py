# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorderTraversal(root):
    arr = []

    def inOrderR(root):
        if(root is None):
            return

        inOrderR(root.left)
        arr.append(root.val)
        inOrderR(root.right)

    inOrderR(root)
    return arr
