class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None
        self.lenght = 0


    def append(self, data):
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(data)
            self.lenght += 1
        else: 
            self.head = Node(data)
            self.lenght += 1


    def __len__(self):
        return self.lenght


    def __setitem__(self, index, element):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer.next
            else:
                raise IndexError("TESTE")
            if pointer:
                pointer.data = element
            else:
                raise IndexError("Teste")


    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("TESTE")
            if pointer:
                return pointer.data
            raise IndexError("TESTE")


    def index(self, element):
        pointer = self.head
        i = 0
        while pointer:
            if pointer.data == element:
                return i 
            pointer = pointer.next
            i += 1
        raise ValueError("teste")
    
    def insert(self, index, element):
        if index == 0:
            node = Node(element)
            node.next = self.head 
            self.head = node
        else:
            pointer = self.head 
            for i in range(index-1):
                if pointer:
                    pointer = pointer.next 
                else:
                    raise IndexError()
                node = Node(element)
                node.next = pointer.next
                pointer.next = node
                self.lenght += 1
            


alist = LinkedList()
alist.append(1)
alist.append(5)
print(len(alist))

var = alist[1]

print(var)
