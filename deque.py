class Deque:
    def __init__(self):
        """Cria um deque inicialmente vazio."""
        self._itens = []

    def insert_first(self, elemento):
        """Adiciona um elemento no começo do deque."""
        self._itens.insert(0, elemento)

    def insert_last(self, elemento):
        """Adiciona um elemento no final do deque."""
        self._itens.append(elemento)

    def remove_first(self):
        """Remove e devolve o primeiro elemento."""
        if self.is_empty():
            print("Erro: o deque está vazio, remoção impossível.")
            return None
        return self._itens.pop(0)

    def remove_last(self):
        """Remove e devolve o último elemento."""
        if self.is_empty():
            print("Erro: não existe elemento no final para remover.")
            return None
        return self._itens.pop()

    def first(self):
        """Consulta o primeiro elemento sem removê-lo."""
        if self.is_empty():
            print("Deque vazio.")
            return None
        return self._itens[0]

    def last(self):
        """Consulta o último elemento sem removê-lo."""
        if self.is_empty():
            print("Deque vazio.")
            return None
        return self._itens[-1]

    def is_empty(self):
        """Retorna True caso o deque esteja vazio."""
        return len(self._itens) == 0

    def size(self):
        """Informa a quantidade de elementos armazenados."""
        return len(self._itens)

    def __str__(self):
        return f"Deque({self._itens})"


if __name__ == "__main__":
    fila = Deque()

    print("Execução das operações do Deque:")
    print("1) insert_last(10)")
    fila.insert_last(10)
    print(fila)

    print("2) insert_last(20)")
    fila.insert_last(20)
    print(fila)

    print("3) insert_first(5)")
    fila.insert_first(5)
    print(fila)

    print("4) remove_last() =>", fila.remove_last())
    print(fila)

    print("5) remove_first() =>", fila.remove_first())
    print(fila)

    print("6) insert_last(30)")
    fila.insert_last(30)
    print(fila)

    print("7) insert_first(1)")
    fila.insert_first(1)
    print(fila)

    print("8) first() =>", fila.first())
    print("9) last() =>", fila.last())
    print("10) size() =>", fila.size())
    print("11) is_empty() =>", fila.is_empty())

    print("12) remove_first() =>", fila.remove_first())
    print(fila)

    print("13) remove_last() =>", fila.remove_last())
    print(fila)

    print("14) remove_last() =>", fila.remove_last())
    print(fila)

    print("15) remove_last() com deque vazio =>", fila.remove_last())
    print("16) remove_first() com deque vazio =>", fila.remove_first())

    print("Estado final:", fila)