from __future__ import annotations
from typing import Optional
import math


class Vector:
    """
    representation of a vector in the cartesian plane
    """
    def __init__(self, start: Optional[tuple]=(0,0), end: Optional[tuple]=(0,0)):
        self.start = start
        self.end = end
    
    def __str__(self) -> str:
        return f'Vector:{self.start}, {self.end} - {self.length}'
    
    def __add__(self, v2: Vector) -> Vector:
        if not isinstance(v2, Vector):
            raise ValueError('Addition is only implemented for two vectors')
        return Vector(
                start=(
                    self.start[0] + v2.start[0],
                    self.start[1] + v2.start[1]),
                end=(
                    self.end[0] + v2.end[0],
                    self.end[1] + v2.end[1])
            )
    
    def __eq__(self, v2: Vector) -> bool:
        if not isinstance(v2, Vector):
            raise ValueError('Equality is only implemented for two vectors')
        return self.start == v2.start and self.end == v2.end
    
    @property
    def length(self) -> float:
        """
        returns the length of the vector
        """
        return math.sqrt((self.start[0] - self.end[0])**2 + (self.start[1] - self.end[1])**2)

    def center(self: Vector) -> Vector:
        """
        returns an equivalent vector but with start in (0,0)
        """
        new_end = (self.end[0] - self.start[0], self.end[1] - self.start[1])
        return Vector(end=new_end)
    
    def project_x(self) -> Vector:
        """
        Returns the projection over X of the vector
        """
        return Vector(
                start=(self.start[0],0),
                end=(self.end[0],0)
                )

    def project_y(self) -> Vector:
        """
        returns the projection over Y of the vector
        """
        return Vector(
                start=(0,self.start[1]),
                end=(0,self.end[1]),
                )
    
IDENTITY = Vector()
CANONIC_X = Vector(start=(0,0), end=(1,0))
CANONIC_Y = Vector(start=(0,0), end=(0,1))



