# Given the head of a singly linked list, reverse the list, and return the reversed list.

 def reverseList(head):
      curr_node, prev, nextt = head, None, None
       while curr_node:
            # Making changes to the node
            nextt = curr_node.next
            curr_node.next = prev

            # Traversing through the Linked List
            prev = curr_node
            curr_node = nextt
        head = prev
        return head
