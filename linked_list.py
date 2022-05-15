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

ll = LinkedList(["1","2","3","4","5"])
print(ll)


