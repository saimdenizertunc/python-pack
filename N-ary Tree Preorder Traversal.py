# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
import math


def preorder(root):
    def depth_first(node, ans):
        ans.append(node.val)
        for child in node.children:
            depth_first(child, ans)
    ans = []
    if root == None:
        return ans
    depth_first(root, ans)
    return ans
