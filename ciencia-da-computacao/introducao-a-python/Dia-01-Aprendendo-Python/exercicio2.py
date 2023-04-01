def mean(numbers):
    total = 0
    for number in numbers:
        total = number + total
    return total / len(numbers)
