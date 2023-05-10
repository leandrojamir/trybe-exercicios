# exercico1.2
#  Vamos começar a nossa memória principal, ou memória RAM: para isso crie um
# arquivo main_memory.py e adicione o conteúdo abaixo nela.
# Implemente os métodos get e load.

#  No load você adicionará (append) o elemento passado (value) à lista
# loaded_memory.
#  No get você retornará o valor presente na posição dada (index) na lista
# loaded_memory. Se o valor não existir ou não for numérico, retorne 0.


class MainMemory:
    def __init__(self):
        self.clean()

    def load(self, value):
        self.loaded_memory.append(value)

    def get(self, index):
        try:
            return float(self.loaded_memory[index])
        except IndexError:
            return 0

    def clean(self):
        self.loaded_memory = []
