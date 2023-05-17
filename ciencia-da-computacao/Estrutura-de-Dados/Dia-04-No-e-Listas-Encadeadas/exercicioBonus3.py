# Exercício 3:
#  Remover duplicatas de uma LinkedList, atividade extraída e adaptada do
# LeetCode. Nesta atividade será necessário implementar um algoritmo que
# receba uma LinkedList como argumento e retorne uma nova lista sem elementos
# duplicados. Esta função deve respeitar a complexidade O(n).

# Exemplo:
# input: 1 -> 1 -> 2
# saída: 1 -> 2
# input: 1 -> 1 -> 2 -> 3 -> 3
# saída: 1 -> 2 -> 3


from .exercicio1 import LinkedList


def delete_duplicates(linked_list):
    list_with_unique_elements = LinkedList()

    while linked_list:
        current_node = linked_list.remove_first()
        if list_with_unique_elements.index_of(current_node.value) == -1:
            list_with_unique_elements.insert_last(current_node.value)

    return list_with_unique_elements
