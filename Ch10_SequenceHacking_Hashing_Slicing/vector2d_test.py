import unittest
import reprlib
from array import array
import math
import numbers
from vector2d import Vector


class TestVector(unittest.TestCase):
    def setUp(self):
        components = [1.0, 2.0, 3.0]
        self.vector = Vector(components)

    def test_init(self):
        self.assertEqual(self.vector._components, array('d', [1.0, 2.0, 3.0]))
        self.assertEqual(self.vector.typecode, 'd')

    def test_iter(self):
        self.assertEqual(list(iter(self.vector)), [1.0, 2.0, 3.0])

    def test_abs(self):
        self.assertAlmostEqual(abs(self.vector), math.sqrt(14.0))

    def test_bool(self):
        self.assertTrue(bool(self.vector))
        self.assertFalse(bool(Vector([0.0, 0.0, 0.0])))

    def test_len(self):
        self.assertEqual(len(self.vector), 3)

    def test_getitem(self):
        self.assertEqual(self.vector[0], 1.0)
        self.assertEqual(list(self.vector[1:3]), [2.0, 3.0])
        self.assertTrue(type(self.vector[1:3]) == Vector)

    def test_repr(self):
        components = reprlib.repr(self.vector._components)
        components = components[components.find('['): -1]
        self.assertEqual(repr(self.vector), f'Vector({components})')

    def test_str(self):
        self.assertEqual(str(self.vector), '(1.0, 2.0, 3.0)')


if __name__ == '__main__':
    unittest.main()
