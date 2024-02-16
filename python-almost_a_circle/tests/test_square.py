import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):

    def test_square__init(self):
        s1 = Square(5, 2, 3, 1)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

        s2 = Square(3, 1)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s2.size, 3)
        self.assertEqual(s2.x, 1)
        self.assertEqual(s2.y, 0)

        with self.assertRaises(ValueError):
            s3 = Square(0, 5)

        with self.assertRaises(TypeError):
            s4 = Square(5, "x")

    def test_size_getter_setter(self):
        s1 = Square(5)
        s1.size = 10
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)

        with self.assertRaises(ValueError):
            s1.size = 0

        with self.assertRaises(TypeError):
            s1.size = "size"

    def test_str(self):
        s1 = Square(4, 2, 1, 12)
        self.assertEqual(str(s1), "[Square] (12) 2/1 - 4")

        s2 = Square(3, 1)
        self.assertEqual(str(s2), "[Square] (2) 1/0 - 3")

    def test_update(self):
        s1 = Square(4, 2, 1, 12)
        s1.update(13, 5, 3, 4)
        self.assertEqual(s1.id, 13)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)

        s2 = Square(3, 1)
        s2.update(size=2, x=2)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s2.x, 2)

    def test_to_dictionary(self):
        s1 = Square(4, 2, 1, 12)
        expected_dict = {'id': 12, 'size': 4, 'x': 2, 'y': 1}
        self.assertEqual(s1.to_dictionary(), expected_dict)

        s2 = Square(3, 1)
        expected_dict = {'id': 2, 'size': 3, 'x': 1, 'y': 0}
        self.assertEqual(s2.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
