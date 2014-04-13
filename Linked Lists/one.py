class LinkedList(object):

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
        
ll = LinkedList()
ll.add(Node(5))
ll.add(Node(6))
print ll.to_str()

#
# 2.1
#
# Write code to remove duplicates from an unsorted linked list
#
def remove_duplicates(ll):
    head = ll.nodes[0]
    while head != None:
         
