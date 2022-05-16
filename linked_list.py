class Node:
    '''
    used for creating individual nodes of LinkedList
    '''
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str: # repr is string representation of file
        return self.data

class LinkedList:
    '''
    Used to initialize the LinkedList with head as None
    '''
    def __init__(self, nodes = None) -> None:
        self.head = None

        if nodes is not None:
            '''
            creating ll's quickly
            ll = LinkedList(["1","2","3","4","5"])
            print(ll)
            '''
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return '->'.join(nodes)

    def __iter__(self):
        '''
        used for iterating through the ll
        '''
        node = self.head
        while node is not None:
            yield node          # for understanding yield = https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
            node = node.next

    def add_to_start(self, node):
        '''
        Add element to the begining of the Linked List
        '''
        node.next = self.head
        self.head = node

    def add_to_end(self, node):
        '''
        Add element to the end of list
        '''
        if self.head is None:
            self.head = node
        
        for current_node in self:
            pass
        
        current_node.next = node


ll = LinkedList(["1","2","3","4","5"])
print(ll)
first_node = Node("0")
ll.add_to_start(first_node)
print(ll)
last_node = Node("6")
ll.add_to_end(last_node)
print(ll)

