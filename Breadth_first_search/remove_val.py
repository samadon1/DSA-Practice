

class Node:
    def __init__(self, val, next = None):

        self.val = val
        self.next = next


def remove_node(head, val):
    dummy = Node(val = None, next = head)
    prev, curr = dummy, dummy

    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
            break
   
        curr = curr.next

    return dummy.next.val


node1 = Node(1) ; node2 = Node(1) ; node3 = Node(3) ; node4 = Node(4) ; node5 = Node(5) ;node6 = Node(6) ;node7 = Node(7)
node1.next = node2 ; node2.next = node3 ; node3.next = node4 ; node4.next = node5 ; node5.next = node6 ; node6.next = node7

Ll = node1

print(remove_node(Ll, 1))