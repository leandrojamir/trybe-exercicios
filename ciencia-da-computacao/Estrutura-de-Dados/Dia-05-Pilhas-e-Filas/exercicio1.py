#  Baseado nos conhecimentos adquiridos nesta seção, e para relembrar as TADs
# vistas em aulas passadas, implemente as seguintes TADs, utilizando a lista
# como a estrutura interna:

# Para este desafio, é necessário efetuar o import das classes LinkedList e
# Node e utilizar seus métodos de acesso para simular uma fila, respeitando o
# padrão FIFO.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.__length = 0

    # a. A operação clear nos permite remover todos os Nodes da lista;
    def clear(self):
        while not self.is_empty():
            self.remove_first()

    #  b. A operação __get_node_at nos permite acessar o Node em qualquer
    # posição da lista.
    def __get_node_at(self, position):
        value_to_be_returned = self.head_value
        if value_to_be_returned:
            while position > 0 and value_to_be_returned.next:
                value_to_be_returned = value_to_be_returned.next
                position -= 1
        return value_to_be_returned

    # Após criada as operações anteriores, refatore os seguintes métodos para
    # que utilizem a __get_node_at ante iterações:
    # insert_at;
    def insert_at(self, value, position):
        if position < 1:
            return self.insert_first(value)
        if position >= len(self):
            return self.insert_last(value)
        current_value = self.__get_node_at(position - 1)
        next_value = Node(value)
        next_value.next = current_value.next
        current_value.next = next_value
        self.__length += 1

    # insert_last;
    def insert_last(self, value):
        if self.is_empty():
            return self.insert_first(value)

        new_last_value = Node(value)
        actual_last_value = self.__get_node_at(len(self) - 1)
        actual_last_value.next = new_last_value
        self.__length += 1

    # remove_last;
    def remove_last(self):
        if len(self) <= 1:
            return self.remove_first()

        previous_to_be_removed = self.__get_node_at(len(self) - 2)
        value_to_be_removed = previous_to_be_removed.next

        previous_to_be_removed.next = None
        self.__length -= 1
        return value_to_be_removed

    # remove_at;
    def remove_at(self, position):
        if position < 1:
            return self.remove_first()
        if position >= len(self):
            return self.remove_last()

        previous_to_be_removed = self.__get_node_at(position - 1)

        value_to_be_removed = previous_to_be_removed.next
        previous_to_be_removed.next = value_to_be_removed.next
        value_to_be_removed.next = None
        self.__length -= 1

        return value_to_be_removed

    # get_element_at.
    def get_element_at(self, position):
        value_returned = None
        value_to_be_returned = self.__get_node_at(position)
        if value_to_be_returned:
            value_returned = Node(value_to_be_returned.value)
        return value_returned


# 🚀 Exercício 1:
# Filas: crie uma classe Queue, onde deve conter as
# operações: enqueue, dequeue, peek e is_empty.


class Queue:
    def __init__(self):
        self.__data = LinkedList()

    def is_empty(self):
        return not len(self.__data)

    def enqueue(self, value):
        self.__data.insert_last(value)

    def dequeue(self):
        return self.__data.remove_first()

    def peek(self):
        return self.__data.get_element_at(0)
