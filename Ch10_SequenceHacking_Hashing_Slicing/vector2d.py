# multidimensional Vector class implemented as a sequence with proper functionality
# supporting slicing, aggregate hashing, custom formatting
import reprlib
from array import array
import math
import numbers


class Vector:
    typecode = 'd'  # 'd' = double precision floating point (min 8 bytes)

    def __init__(self, components):
        self._components = array(self.typecode, components)  # array of components

    def __iter__(self):
        return iter(self._components)  # return an iterator over components to allow iteration over Vector

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    # implementing __len__ and __getitem__ makes Vector a 'Sequence Protocol'
    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(list(self._components[index]))
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            raise TypeError(f'{cls.__name__} indices must be integer')

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['): -1]  # e.g. [0.0, 1.0, 2.0, 3.0, 4.0, ...]
        return f'Vector({components})'

    def __str__(self):  # str repr is designed to be readable to the non-programmer
        return str(tuple(self))







