def rotate(matrix: list[list[int]]) -> list[list[int]]:

    new_matrix = []
    for new_line in zip(*matrix):
        new_matrix.append(list(reversed(new_line)))

    return new_matrix


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rotate(matrix))
