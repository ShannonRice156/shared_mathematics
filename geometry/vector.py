"""
This module provides classes for vector operations in both 2D and 3D space.

Classes:
    vector_base: Abstract base class representing a vector.
    vector: A class representing a vector in 2D space. Inherits from vector_base.
    vector_3D: A class representing a vector in 3D space. Inherits from vector_base.

"""
from __future__ import annotations
from abc import ABC


class vector_base(ABC):
    """Abstract base class representing a vector."""

    def transpose(self) -> None:
        """Transposes the vector by swapping its x and y coordinates."""
        temp_x = self._dimensions[0]
        temp_y = self._dimensions[1]
        self.dimensions = (temp_y, temp_x)

    @property
    def dimensions(self) -> tuple:
        """Getter property that returns the dimensions of the vector."""
        return self._dimensions

    @dimensions.setter
    def dimensions(self, new_dimensions: tuple) -> None:
        """Setter property that sets the dimensions of the vector."""
        self._dimensions = new_dimensions


class Vector(vector_base):
    """A class representing a vector. Inherits from vector_base which provides basic vector operations"""

    def __init__(self, x: float, y: float) -> None:
        """Initializes a vector instance with given x and y coordinates."""
        super().__init__()
        self.x = x
        self.y = y
        self.dimensions = (1, 2)

    def __add__(self, addition_vector: Vector) -> Vector:
        """Adds another vector to the current vector and returns the result."""
        new_x = addition_vector.x + self.x
        new_y = addition_vector.y + self.y
        return Vector(new_x, new_y)

    def __iadd__(self, addition_vector: Vector) -> Vector:
        """Adds another vector to the current vector in-place."""
        self.x += addition_vector.x
        self.y += addition_vector.y
        return self

    def __mul__(self, multiplication_vector: Vector) -> Vector:
        """Multiplies the current vector by another vector and returns the result."""
        new_x = multiplication_vector.x * self.x
        new_y = multiplication_vector.y * self.y
        return Vector(new_x, new_y)

    def __imul__(self, multiplication_vector: Vector) -> Vector:
        """Multiplies the current vector by another vector in-place."""
        self.x *= multiplication_vector.x
        self.y *= multiplication_vector.y
        return self

    def __sub__(self, subtraction_vector: Vector) -> Vector:
        """Subtracts another vector from the current vector and returns the result."""
        new_x = self.x - subtraction_vector.x
        new_y = self.y - subtraction_vector.y
        return Vector(new_x, new_y)

    def __isub__(self, subtraction_vector: Vector) -> Vector:
        """Subtracts another vector from the current vector in-place."""
        self.x -= subtraction_vector.x
        self.y -= subtraction_vector.y
        return self


class Vector_3D(vector_base):
    """A class representing a 3d vector with an x, y and z axis. Inherits from vector_base which provides basic vector operations"""

    def __init__(self, x: float, y: float, z: float) -> None:
        """Initializes a vector instance with given x, y and z coordinates."""

        super().__init__()
        self.x = x
        self.y = y
        self.z = z
        self.dimensions = (1, 3)

    def __add__(self, addition_vector: Vector_3D) -> Vector_3D:
        """Adds another vector to the current vector and returns the result."""

        new_x = addition_vector.x + self.x
        new_y = addition_vector.y + self.y
        new_z = addition_vector.z + self.z
        return Vector_3D(new_x, new_y, new_z)

    def __iadd__(self, addition_vector: Vector_3D) -> Vector_3D:
        """Adds another vector to the current vector in-place."""

        self.x += addition_vector.x
        self.y += addition_vector.y
        self.z += addition_vector.z
        return self

    def __mul__(self, multiplication_vector: Vector_3D) -> Vector_3D:
        """Multiplies the current vector by another vector and returns the result."""
        new_x = self.x * multiplication_vector.x
        new_y = self.y * multiplication_vector.y
        new_z = self.z * multiplication_vector.z
        return Vector_3D(new_x, new_y, new_z)

    def __imul__(self, multiplication_vector: Vector_3D) -> Vector_3D:
        """Multiplies the current vector by another vector in-place."""
        self.x *= multiplication_vector.x
        self.y *= multiplication_vector.y
        self.z *= multiplication_vector.z
        return self

    def __sub__(self, subtraction_vector: Vector_3D) -> Vector_3D:
        """Subtracts another vector from the current vector and returns the result."""
        new_x = self.x - subtraction_vector.x
        new_y = self.y - subtraction_vector.y
        new_z = self.z - subtraction_vector.z
        return Vector_3D(new_x, new_y, new_z)

    def __isub__(self, subtraction_vector: Vector_3D) -> Vector_3D:
        """Subtracts another vector from the current vector in-place."""
        self.x -= subtraction_vector.x
        self.y -= subtraction_vector.y
        self.z -= subtraction_vector.z
        return self
