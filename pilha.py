class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.topo = None
        self._size = 0

    def inverter_string(self, texto):
        pilha = []

        for letra in texto:
            pilha.append(letra)

            invertida = ""
        
        while pilha:
            invertida += pilha.pop()
        return invertida

print(Stack().inverter_string("algoritmo"))