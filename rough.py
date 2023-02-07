from array import array
import reprlib


class Vector:
    typecode = 'd'

    def __init__(self, cs):
        self._components = cs

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['): -1]
        return f'Vector({components})'

    def __eq__(self, other):
        return tuple(self) == tuple(other)  # requires implementation of __iter__


cs = [1.0, 2.0, 3.0, 4.0]
v1 = Vector(cs)
v2 = Vector(cs)

print(v1 == v2, '\n', v1 is v2)

