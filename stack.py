
class Stack:
  def __init__(self):
    self.items = []  # definindo o dado de manipulacao como uma lista vazia
    # consequentemente estipulando que a chamada da funcao Stack() cria uma lista vazia

  def isEmpty(self):
    # definicao da funcao isEmpty, que retorna um valor booleano para a analise da quantidade de itens que a lista contem
    return self.items == []

  def push(self, item):
    # definicao da funcao .push(item), que insere o dado "item" ao final da pilha
    self.items.append(item)

  def pop(self):
    # definicao da funcao .pop(), que realiza a remocao do item mais ao topo da pilha[, retornando este item]
    return self.items.pop()

  def peek(self):
    # definicao da funcao .peek(), que retorna o item do topo da pilha
    return self.items[-1]

  def size(self):
    # definicao da funcao .size(), que retorna a quantidade de itens da pilha ate o momento da chamada
    return len(self.items)
