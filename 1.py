from typing import List
class Matrix:
    def __init__(self, matrix_data: List[List]):
        self._mtr = matrix_data
        m_rows = len(self._mtr)
        self.__matrix_size = frozenset([(m_rows, len(row)) for row in self._mtr])
        if len(self.__matrix_size) != 1:
            raise ValueError("Недопустимый размер матрицы")
    def __add__(self, other: "Matrix") -> "Matrix":
        if not isinstance(other, Matrix):
            raise TypeError(f"'{other.__class__.__name__}' "
                            f"несовместимый тип объекта")
        if self.__matrix_size != other.__matrix_size:
            raise ValueError(f"Разница в размерах матрицы")
        result = []
        for item in zip(self._mtr, other._mtr):
            result.append([sum([j, k]) for j, k in zip(*item)])
        return Matrix(result)
    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self._mtr])
if __name__ == '__main__':
    matrix1 = Matrix([[2, 2], [5, 4]])
    print(matrix1, '\n')
    matrix2 = Matrix([[15, 32], [80, 90]])
    print(matrix2, '\n')
    print(matrix1 + matrix2)

