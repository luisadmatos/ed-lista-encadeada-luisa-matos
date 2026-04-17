
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, elem):
        node = Node(elem)
        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1

    def dequeue(self):
        if self._size > 0:
            elem = self.head.data
            self.head = self.head.next
            self._size -= 1

            # Corrige quando a fila fica vazia
            if self.head is None:
                self.tail = None

            return elem
        raise IndexError("The queue is empty")

    def front(self):
        if self._size > 0:
            return self.head.data
        raise IndexError("The queue is empty")

    def __len__(self):
        return self._size

    def show(self):
        pointer = self.head
        while pointer:
            print(pointer.data)
            pointer = pointer.next


class Process:
    def __init__(self, name, burst_time):
        self.name = name
        self.remaining_time = burst_time

    def __str__(self):
        return f"{self.name} (restante: {self.remaining_time})"


def round_robin(queue, quantum):
    time = 0

    print("\n=== Início da execução Round-Robin ===\n")

    while len(queue) > 0:
        process = queue.dequeue()

        print(f"Tempo {time}: Executando {process.name}")

        if process.remaining_time <= quantum:
            time += process.remaining_time
            print(f"{process.name} finalizado no tempo {time}\n")
        else:
            process.remaining_time -= quantum
            time += quantum

            print(f"{process.name} não terminou, resta {process.remaining_time}")
            print(f"{process.name} volta para o final da fila\n")

            queue.enqueue(process)

    print(f"=== Todos os processos finalizados em tempo total = {time}")


# Teste
if __name__ == "__main__":
    fila = Queue()

    fila.enqueue(Process("P1", 10))
    fila.enqueue(Process("P2", 5))
    fila.enqueue(Process("P3", 8))

    quantum = 3

    round_robin(fila, quantum)