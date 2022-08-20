"""
Given the head of a singly linked list, write a function to determine if the linked list has a cycle
in it or not.

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def hasCycle(head):
    fast = head
    slow = head

    while fast and slow:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            return True
    return False

node1 = Node(1) ; node2 = Node(2) ; node3 = Node(3) ; node4 = Node(4) ; node5 = Node(5) ;node6 = Node(6) ;node7 = Node(7)
node1.next = node2 ; node2.next = node3 ; node3.next = node4 ; node4.next = node5 ; node5.next = node6 ; node6.next = node7; node7.next = node3

Ll = node1

print(hasCycle(Ll))