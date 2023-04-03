from exercicio1 import fizzbuzz


def test_fizzbuzz_should_return_list_of_numbers():
    n = 2
    assert fizzbuzz(n) == [1, n]


def test_fizzbuzz_divisible_by_three_should_be_fizz():
    n = 3
    assert fizzbuzz(n)[n-1] == "Fizz"


def test_fizzbuzz_divisible_by_five_should_be_buzz():
    n = 5
    assert fizzbuzz(n)[n-1] == "Buzz"


def test_fizzbuzz_divisible_by_five_and_three_should_be_fizzbuzz():
    n = 15
    assert fizzbuzz(n)[n-1] == "FizzBuzz"
