import numpy as np
import time
# For n >= 1 [[1, 1], [1, 0]]^n = [[F(n+1), F(n)], [F(n), F(n-1)]]
# [f(n), f(n-1)] = [[1, 1], [1, 0]]^(n-1) * [f(1), f(0)]


def fib(n: int):
    # [[1, 1], [1, 0]]
    base_matrix = np.array([[1, 1], [1, 0]], dtype=np.float64)
    # [f(1), f(0)]
    initial_vector = np.array([1, 0], dtype=np.float64)
    if n <= 1:
        return initial_vector[0] if n == 0 else initial_vector[1]

    result_matrix = base_matrix

    # [[1, 1], [1, 0]]^(n-1)
    for _ in range(n-2):
        result_matrix = np.dot(result_matrix, base_matrix)

    result_vector = np.dot(result_matrix, initial_vector)
    return result_vector[0]


def matrix_power(matrix, n):
    result = np.eye(len(matrix))
    while n > 0:
        if n % 2 == 1:
            result = np.dot(result, matrix)
        matrix = np.dot(matrix, matrix)
        n //= 2
    return result


def fib_fast_exponentiation(n):
    base_matrix = np.array([[1, 1], [1, 0]], dtype=np.float64)
    initial_vector = np.array([1, 0], dtype=np.float64)
    if n <= 1:
        return initial_vector[0] if n == 0 else initial_vector[1]
    else:
        result_matrix = matrix_power(base_matrix, n-1)
        result_vector = np.dot(result_matrix, initial_vector)
        return result_vector[0]


def execute(fn, n):
    print(f"Executing {fn.__name__}({n}) starting at {time.ctime()}")
    result = fn(n)
    print(f"Result: {result}")
    print(f"Ending at: {time.ctime()}")


if __name__ == "__main__":
    execute(fib, 200)
    execute(fib_fast_exponentiation, 200)
