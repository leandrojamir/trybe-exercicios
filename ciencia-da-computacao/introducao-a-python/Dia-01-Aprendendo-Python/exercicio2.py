# Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.

def mean(numbers):
    total = 0
    for number in numbers:
        total = number + total
    return total / len(numbers)
