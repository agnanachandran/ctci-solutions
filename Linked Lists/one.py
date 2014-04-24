class LinkedList(object):

    # Really only needs to maintain reference to first and/or last node; no need for array?
    def __init__(self):
        self.nodes = []

    def add(self,node):
        self.nodes.append(node)
        length = len(self.nodes)
        if length > 1:
            self.nodes[length-2].next = node

    def to_str(self):
        for node in self.nodes:
            print node.val

class Node(object):

    def __init__(self, val):
        self.next = None
        self.val = val

#
# 2.1
#
# Write code to remove duplicates from an unsorted linked list
# No temporary buffer?
def remove_duplicates(ll):
    head = ll.nodes[0]
    seen = set()
    while head != None:
        if head.val not in seen:
            seen.add(head.val)
        else:
            head.val = None
        head = head.next
        
ll = LinkedList()
ll.add(Node(5))
ll.add(Node(6))
ll.add(Node(6))
print ll.to_str()
remove_duplicates(ll)
print ll.to_str()

