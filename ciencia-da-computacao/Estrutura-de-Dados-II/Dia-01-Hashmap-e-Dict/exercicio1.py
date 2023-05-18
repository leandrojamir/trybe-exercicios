#  Iremos realizar um exercício que utiliza vários dos conceitos, métodos e
# estratégias vistas ao longo da aula. Lembre-se de pensar sobre o problema e
# anotar todas as situações que podem ocorrer.

#  O exercício foi retirado do banco de questões utilizadas em processos de
# contratação de grandes empresas (questões liberadas para estudo). A questão
# não é trivial. Caso você emperre, não hesite em consultar a resposta.
# A gente aprende muito lendo código de outras pessoas.

# Exercício 1 - Google
#  Uma certa empresa tem uma estrutura hierarquizada onde cada pessoa reporta
# a uma única outra pessoa. Cada pessoa tem um score que é o total de pessoas
# que estão abaixo dela, incluindo subordinados de seus subordinados, além
# dela própria. Isso significa que uma pessoa que não tem nenhuma equipe tem
# score 1. Uma pessoa com apenas um subordinado e esse subordinado não tem
# equipe, tem score 2.

# Escreva um método que calcule o score de uma determinada pessoa.

#  Dica: para saber o score de uma pessoa, você precisa saber o score das
# pessoas da equipe dela, correto? Qual estratégia utiliza a mesma função
# dentro dela própria?

# Exemplo de subordinados:
# - 1 => 5 (score 2) + 1 (score 3) + 1 (score dele próprio) = 7
# - 2 => 4 (score 4) + 1 (score dele próprio) = 5
# - 3 => 1 (score dele próprio)
# - 4 => 2 (score 5) + 1 (score 6) + 1 (score dele próprio) = 4
# - 5 => 1 (score 7) + 1 (score dele próprio) = 2
# - 6 => 1 (score dele próprio)
# - 7 => 1 (score dele próprio)


# score da pessoa 5 = 1 + score da pessoa 7 (1)
# score da pessoa 7 = 1
# recursividade


def score(subordinates, person):
    this_score = 1

    for subordinate in subordinates[person]:
        this_score += score(subordinates, subordinate)

    return this_score


if __name__ == "__main__":
    subordinates = {
        1: [2, 3],
        2: [4],
        3: [],
        4: [5, 6],
        5: [7],
        6: [],
        7: [],
    }

    print(score(subordinates, 1))
    print(score(subordinates, 2))
    print(score(subordinates, 3))
    print(score(subordinates, 4))
    print(score(subordinates, 5))
    print(score(subordinates, 6))
    print(score(subordinates, 7))

# Follow-ups:

# 1 - Caso a empresa precise fazer essa consulta frequentemente, como você pode
# tornar essas consultas mais eficientes? Como você pode guardar o resultado
# de consultas anteriores?

# 2 - Escreva um método para incluir uma nova pessoa na equipe de uma outra
# pessoa. Seu método deve considerar que cada pessoa pode ter no máximo k
# pessoas em seu time. Se o time estiver cheio, a nova contratada pode ser
# alocada na equipe de qualquer pessoa abaixo dela, não precisando ser na
# equipe imediatamente abaixo.

# 3 - Se você adicionar uma nova contratação à lista de subordinadas, a
# estrutura que você fez no follow-up 1 está desatualizada. Modifique suas
# funções para que essa estrutura seja atualizada junto com a adição de uma
# nova contratação. Faça isso sem rodar de novo a função score() e lembre-se de
# atualizar todos os scores desde a pessoa da presidência até a equipe que
# a nova contratação entrou.
