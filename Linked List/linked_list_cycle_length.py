"""
Given the head of a linked list with a cycle, find the length of the cycle
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def cycleLenght(head):
    slow = head                 #set slow and fast pointer to head
    fast = head

    while fast and slow:        #while slow and fast are not none
        fast = fast.next.next   # move fast 2 steps
        slow = slow.next        #move slow 1 step

        if slow == fast:        #if fast meets slow;there's a cycle
            return slowLength(slow)     # return length of cycle
    
    return False

def slowLength(slow):
    current = slow
    length = 0

    while current:
        current = current.next
        length += 1

        if current == slow:
            return length


node1 = Node(1) ; node2 = Node(2) ; node3 = Node(3) ; node4 = Node(4) ; node5 = Node(5) ;node6 = Node(6) ;node7 = Node(7)
node1.next = node2 ; node2.next = node3 ; node3.next = node4 ; node4.next = node5 ; node5.next = node6 ; node6.next = node7; node7.next = node3

Ll = node1

print(cycleLenght(Ll))
        
