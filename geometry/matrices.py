"""
This module provides classes for vector operations in both 2D and 3D space.

Classes:
    Matrix: A class representing a matrix.

"""

from __future__ import annotations

def check_dimensions(current: Matrix, other: Matrix):
    """A function which checks the dimensions match for any two given matrices"""
    if current.shape() != other.shape():
        raise ValueError("Dimensions do not match.")


class Matrix:
    """A class representing a vector. Inherits from vector_base which provides basic vector operations"""

    def __init__(self, rows: int, cols: int) -> None:
        """Initialize a matrix object and its data."""
        self.__rows = rows
        self.__cols = cols
        self.__data = [[0] * cols for _ in range(rows)]

    def __str__(self) -> str:
        """Get the string representation of the matrix."""
        result = ""
        for row in self.__data:
            result += " ".join(str(element) for element in row) + "\n"
        return result

    def __getitem__(self, index: int) -> float:
        """Get the value at the specified index of the matrix."""
        return self.__data[index]

    def __setitem__(self, index: int, value: float) -> None:
        """set the value at the specified index of the matrix."""
        self.__data[index] = value

    def shape(self) -> tuple:
        """Get the shape of the matrix."""
        return self.__rows, self.__cols

    def transpose(self):
        """Transpose the matrix"""
        result = Matrix(self.__cols, self.__rows)
        for i in range(self.__rows):
            for j in range(self.__cols):
                result[j][i] = self.__data[i][j]
        return result

    def __add__(self, other: Matrix) -> Matrix:
        """Add two matrices element-wise."""
        check_dimensions(self, other)
        result = Matrix(self.__rows, self.__cols)
        for i in range(self.__rows):
            for j in range(self.__cols):
                result[i][j] = self.__data[i][j] + other[i][j]
        return result

    def __iadd__(self, other: Matrix) -> Matrix:
        """Add another matrix to the current matrix in-place."""
        check_dimensions(self, other)
        for i in range(self.__rows):
            for j in range(self.__cols):
                self[i][j] = self.__data[i][j] + other[i][j]
        return self

    def __sub__(self, other: Matrix) -> Matrix:
        """Subtract another matrix from the current matrix in-place."""
        check_dimensions(self, other)
        result = Matrix(self.__rows, self.__cols)
        for i in range(self.__rows):
            for j in range(self.__cols):
                result[i][j] = self.__data[i][j] - other[i][j]
        return result

    def __isub__(self, other: Matrix) -> Matrix:
        """Subtract another matrix from the current matrix in-place."""
        check_dimensions(self, other)

        for i in range(self.__rows):
            for j in range(self.__cols):
                self[i][j] = self.__data[i][j] - other[i][j]
        return self
    