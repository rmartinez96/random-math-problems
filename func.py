# Raul Martinez
# Description: Random functions that I find interesting. Some code was found online.


# Factorial: 4 => 4 x 3 x 2 x 1 = 24
def factorial(n):
    return factorial(n - 1) * n if n > 1 else 1


# Sequence Sum: 4 => 4 + 3 + 2 + 1 = 10
def seq_sum(n):
    return seq_sum(n - 1) + n if n > 1 else 1


# Fibonacci Sequence: 4 => [1, 1, 2, 3]
def fib(n):
    return [fibh(i) for i in range(n)]


# Fibonacci Sequence Helper
def fibh(n):
    return n if n <= 1 else fibh(n - 1) + fibh(n - 2)


# Pascals Triangle: 4 => [[1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
def pascals_triangle(n):
    line = [1]
    y = [0]
    triangle = []
    triangle.append(line)

    for x in range(n):
        line = [left + right for left, right in zip(line + y, y + line)]
        triangle.append(line)

    return triangle