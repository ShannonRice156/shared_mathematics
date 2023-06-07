"""Module to test all functionality in vector module"""

from geometry.vector import Vector, Vector_3D


def test_vector_addition():
    """Test vector addition."""
    v1 = Vector(2, 3)
    v2 = Vector(4, 5)
    result = v1 + v2
    assert result.x == 6
    assert result.y == 8


def test_vector_in_place_addition():
    """Test in-place vector addition."""
    v1 = Vector(2, 3)
    v2 = Vector(4, 5)
    v1 += v2
    assert v1.x == 6
    assert v1.y == 8


def test_vector_multiplication():
    """Test vector multiplication."""
    v1 = Vector(2, 3)
    v2 = Vector(4, 5)
    result = v1 * v2
    assert result.x == 8
    assert result.y == 15


def test_vector_in_place_multiplication():
    """Test in-place vector multiplication."""
    v1 = Vector(2, 3)
    v2 = Vector(4, 5)
    v1 *= v2
    assert v1.x == 8
    assert v1.y == 15


def test_vector_subtraction():
    """Test vector subtraction."""
    v1 = Vector(4, 5)
    v2 = Vector(2, 3)
    result = v1 - v2
    assert result.x == 2
    assert result.y == 2


def test_vector_in_place_subtraction():
    """Test in-place vector subtraction."""
    v1 = Vector(4, 5)
    v2 = Vector(2, 3)
    v1 -= v2
    assert v1.x == 2
    assert v1.y == 2


def test_vector_transpose():
    """Test vector transposition."""
    v1 = Vector(4, 5)
    v1.transpose()
    assert v1.dimensions == (2, 1)


def test_vector_3D_addition():
    """Test 3D vector addition."""
    v1 = Vector_3D(2, 3, 4)
    v2 = Vector_3D(4, 5, 6)
    result = v1 + v2
    assert result.x == 6
    assert result.y == 8
    assert result.z == 10


def test_vector_3D_in_place_addition():
    """Test in-place 3D vector addition."""
    v1 = Vector_3D(2, 3, 4)
    v2 = Vector_3D(4, 5, 6)
    v1 += v2
    assert v1.x == 6
    assert v1.y == 8
    assert v1.z == 10


def test_vector_3D_multiplication():
    """Test 3D vector multiplication."""
    v1 = Vector_3D(2, 3, 4)
    v2 = Vector_3D(4, 5, 6)
    result = v1 * v2
    assert result.x == 8
    assert result.y == 15
    assert result.z == 24


def test_vector_3D_in_place_multiplication():
    """Test in-place 3D vector multiplication."""
    v1 = Vector_3D(2, 3, 4)
    v2 = Vector_3D(4, 5, 6)
    v1 *= v2
    assert v1.x == 8
    assert v1.y == 15
    assert v1.z == 24


def test_vector_3D_subtraction():
    """Test 3D vector subtraction."""
    v1 = Vector_3D(4, 5, 6)
    v2 = Vector_3D(2, 3, 4)
    result = v1 - v2
    assert result.x == 2
    assert result.y == 2
    assert result.z == 2


def test_vector_3D_in_place_subtraction():
    """Test in-place 3D vector subtraction."""
    v1 = Vector_3D(4, 5, 6)
    v2 = Vector_3D(2, 3, 4)
    v1 -= v2
    assert v1.x == 2
    assert v1.y == 2
    assert v1.z == 2


def test_vector_3D_transpose():
    """Test 3D vector transposition."""
    v1 = Vector_3D(4, 5, 6)
    v1.transpose()
    assert v1.dimensions == (3, 1)
