# Given the head of a linked list and an integer val
# Remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math


def removeElements(head, val):
    dummy_head = ListNode(-math.inf)
    dummy_head.next = head
    curr_node = dummy_head

    while curr_node.next is not None:
        if curr_node.next.val == val:
            curr_node.next = curr_node.next.next
        else:
            curr_node = curr_node.next
    return dummy_head.next
