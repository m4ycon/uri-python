class Queue:
  def __init__(self):
    # inicialização de uma fila vazia, equivalente a função fila = Queue()
    self.items = []

  def isEmpty(self):
    # implementação da funcionalidade que checa se a fila esta vazia ou nao (isEmpty())
    return self.items == []

  def enqueue(self, item):
    # construção da estrutura que adiciona o dado "item" no comeco da fila (enqueue() function)
    self.items.insert(0, item)

  def dequeue(self):
    # implementação da função dequeue(), a qual retira o último elemento da fila quando chamada
    return self.items.pop()

  def size(self):
    # definição do funcionamento da função size(), a qual retorna a quantidade de itens de uma fila, caracterizando o tamanho da mesma ate o momento da chamada
    return len(self.items)
