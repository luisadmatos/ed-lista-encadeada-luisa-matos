class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self._size = 0

    def insert_end(self, elem):
        if self.head:                 
            pointer = self.head         
            while(pointer.next):        
                pointer = pointer.next
            pointer.next = Node(elem)   
        else:
            self.head = Node(elem)      
        self._size = self._size + 1

    def __len__(self):
        return self._size
    
    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")   
        if pointer:
            return pointer.data
        else:
            raise IndexError("list index out of range") 
        
    def __setitem__(self, index, elem):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")   
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")

    def insert_beginning(self, data) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size = self._size + 1

    def remove(self, data) -> None:
        curr = self.head
        prev = None
        found = False

        while curr and not found:
            if curr.data == data:
                found = True
            else:
                prev = curr
                curr = curr.next

        if not found:
            return

        if prev is None:
            self.head = curr.next
        else:
            prev.next = curr.next
        self._size = self._size - 1

    def search(self, data):
        pointer = self.head
        while pointer:
            if pointer.data == data:
                return True
            pointer = pointer.next
        return False

    def print_list(self):
        pointer = self.head
        while pointer:
            print(pointer.data, end=" -> ")
            pointer = pointer.next
        print("None")

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0


lista = LinkedList()
print(lista.is_empty())
lista.insert_end(5)
lista.insert_end(7)
lista.insert_end(9)

lista.insert_beginning(1)
lista.print_list()        
print(lista.size())        
print(lista.search(7))            
print(lista.search(99))          
lista.remove(7)
lista.print_list()                      
print(lista.size())       
print(lista.is_empty())    