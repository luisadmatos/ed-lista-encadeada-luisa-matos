class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.topo = None
        self._size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.topo
        self.topo = new_node
        self._size += 1

    def pop(self):
        if self.topo is None:
            return None
        removed = self.topo
        self.topo = self.topo.next
        self._size -= 1
        return removed.data

    def peek(self):
        if self.topo is None:
            return None
        return self.topo.data

    def __len__(self):
        return self._size

    def inverter_string(self, texto):
        pilha = Stack()

        for letra in texto:
            pilha.push(letra)

        invertida = ""

        while len(pilha) > 0:
            invertida += pilha.pop()

        return invertida


# teste
print(Stack().inverter_string("ALGORITMO"))