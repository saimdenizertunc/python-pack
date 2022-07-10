# Given head which is a reference node to a singly-linked list.
# The value of each node in the linked list is either 0 or 1.
# The linked list holds the binary representation of a number.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def getDecimalValue(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    resl = int("".join(str(x) for x in res), 2)

    return resl
