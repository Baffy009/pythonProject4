"""
1. Напишите функцию для транспонирования матрицы .
"""


def matrix_transp(matrix):
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]


matrix = [[5, 2, 4, 8],
          [2, 3, 4, 12],
          [8, 5, 3, 10],
          [1, 4, 2, 8]
          ]

print(f'исходная матрица:')
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(f'{matrix[i][j]:>{3}}', end=",")
    print()

transp_matrix = matrix_transp(matrix)
# print(f'транспонированная матрица: {matrix_trans(matrix)}')
print('транспонированная матрица:')
for i in range(len(transp_matrix)):
    for j in range(len(transp_matrix[0])):
        print(f'{transp_matrix[i][j]:>{3}}', end=",")
    print()