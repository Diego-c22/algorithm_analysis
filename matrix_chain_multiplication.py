def optimal_matrix_chain_multiplication(p):
    n = len(p) - 1
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]


    for i in range(n):
        m[i][i] = 0


    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k


    def print_optimal_parenthesization(s, i, j):
        if i == j:
            print("A", i + 1, end="")
        else:
            print("(", end="")
            print_optimal_parenthesization(s, i, s[i][j])
            print_optimal_parenthesization(s, s[i][j] + 1, j)
            print(")", end="")

    print("Parentización óptima:", end=" ")
    print_optimal_parenthesization(s, 0, n - 1)
    print()
    return m[0][n - 1]


p = [5, 10, 3, 12, 5, 50, 6]
min_multiplications = optimal_matrix_chain_multiplication(p)
print("Mínimo número de multiplicaciones escalares:", min_multiplications)
