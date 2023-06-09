"""Module to test all functionality in matrix module"""

import pytest
from geometry.matrices import Matrix, check_dimensions

def test_matrix_creation():
    """Test matrix creation."""
    matrix = Matrix(3, 3)
    assert matrix.shape() == (3, 3)
    assert matrix[0] == [0, 0, 0]
    assert matrix[1] == [0, 0, 0]
    assert matrix[2] == [0, 0, 0]

def test_matrix_transpose():
    """Test matrix transposition."""
    matrix = Matrix(2, 3)
    matrix[0] = [1, 2, 3]
    matrix[1] = [4, 5, 6]
    result = matrix.transpose()
    assert result.shape() == (3, 2)
    assert result[0] == [1, 4]
    assert result[1] == [2, 5]
    assert result[2] == [3, 6]

def test_matrix_addition():
    """Test matrix addition."""
    matrix1 = Matrix(2, 2)
    matrix1[0] = [1, 2]
    matrix1[1] = [3, 4]

    matrix2 = Matrix(2, 2)
    matrix2[0] = [5, 6]
    matrix2[1] = [7, 8]

    result = matrix1 + matrix2
    assert result.shape() == (2, 2)
    assert result[0] == [6, 8]
    assert result[1] == [10, 12]

def test_matrix_subtraction():
    """Test matrix subtraction."""
    matrix1 = Matrix(2, 2)
    matrix1[0] = [5, 6]
    matrix1[1] = [7, 8]

    matrix2 = Matrix(2, 2)
    matrix2[0] = [1, 2]
    matrix2[1] = [3, 4]

    result = matrix1 - matrix2
    assert result.shape() == (2, 2)
    assert result[0] == [4, 4]
    assert result[1] == [4, 4]

def test_matrix_addition_in_place():
    """Test in-place matrix addition."""
    matrix1 = Matrix(2, 2)
    matrix1[0] = [1, 2]
    matrix1[1] = [3, 4]

    matrix2 = Matrix(2, 2)
    matrix2[0] = [5, 6]
    matrix2[1] = [7, 8]

    matrix1 += matrix2
    assert matrix1.shape() == (2, 2)
    assert matrix1[0] == [6, 8]
    assert matrix1[1] == [10, 12]

def test_matrix_subtraction_in_place():
    """Test in-place matrix subtraction."""
    matrix1 = Matrix(2, 2)
    matrix1[0] = [5, 6]
    matrix1[1] = [7, 8]

    matrix2 = Matrix(2, 2)
    matrix2[0] = [1, 2]
    matrix2[1] = [3, 4]

    matrix1 -= matrix2
    assert matrix1.shape() == (2, 2)
    assert matrix1[0] == [4, 4]
    assert matrix1[1] == [4, 4]

def test_matrix_invalid_dimensions():
    """Test invalid dimensions."""
    matrix1 = Matrix(2, 3)
    matrix2 = Matrix(3, 2)
    with pytest.raises(ValueError):
        check_dimensions(matrix1, matrix2)

    matrix3 = Matrix(2, 2)
    matrix4 = Matrix(2, 2)
    check_dimensions(matrix3, matrix4)
