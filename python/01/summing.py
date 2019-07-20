def sum_numbers(numbers=None):
    sum = 0
    if (
        isinstance(numbers, list)
        or isinstance(numbers, range)
        or isinstance(numbers, tuple)
    ):
        for i in numbers:
            sum = sum + i
    else:
        for j in range(1, 101):
            sum = sum + j
    return sum

