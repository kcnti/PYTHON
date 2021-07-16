def high_and_low(numbers):
    numbers = numbers.split(" ")
    numbers = list(map(int, numbers))
    _max = max(numbers)
    _min = min(numbers)
    return f'{_max} {_min}'

high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")