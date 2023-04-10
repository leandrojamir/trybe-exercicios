# Exercício de fixação 1
# Além do liquidificador, podemos modelar inúmeros eletrodomésticos, tais
# como: ventilador, batedeira, secador, máquina de lavar e etc.
# Para fixar crie uma objeto da classe Ventilador, semelhante ao exemplo do
# liquidificador.
# Em seguida faça com que a pessoa tenha um ventilador como atributo através
# da composição.
# Crie também um método comprar_ventilador.
# Faça com que o print (__str__) de Pessoa informe se sua instância possui
# ou não um ventilador.


class Ventilador:
    def __init__(self, cor, potencia, tensao, preco):
        self.preco = preco
        self.__cor = cor
        self.__potencia = potencia
        self.__tensao = tensao
        self.__ligado = False

    def cor(self):
        return self.__cor


class Pessoa:
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.ventilador = None

    def comprar_ventilador(self, ventilador):
        if ventilador.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= ventilador.preco
            self.ventilador = ventilador

    def __str__(self):
        if self.ventilador:
            return f"{self.nome} - possui um ventilador."
        return f"{self.nome} - não possui um ventilador."


ventilador_branco = Ventilador("branco", potencia=250, tensao=220, preco=100)
pessoa = Pessoa("Maria", saldo_na_conta=2000)
pessoa.comprar_ventilador(ventilador_branco)

print(pessoa)
