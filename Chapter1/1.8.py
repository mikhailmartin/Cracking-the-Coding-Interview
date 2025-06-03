from itertools import product


def zero_matrix(matrix: list[list[int]]) -> list[list[int]]:

    m = len(matrix)  # количество строк
    n = len(matrix[0])  # количество столбцов

    columns_with_zero = set()
    lines_with_zero = set()

    for x, y in product(range(m), range(n)):
        if matrix[x][y] == 0:
            columns_with_zero.add(x)
            lines_with_zero.add(y)

    for x, y in product(columns_with_zero, range(n)):
        matrix[x][y] = 0
    for x, y in product(range(m), lines_with_zero):
        matrix[x][y] = 0

    return matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 0, 8],
        [9, 10, 11, 12],
    ]
    print(zero_matrix(matrix))
