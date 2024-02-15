import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_init(self):
        # Test the constructor
        s = Square(5, 2, 3, 1)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_str(self):
        # Test the __str__ method
        s = Square(5, 2, 3, 1)
        self.assertEqual(str(s), "[Square] (1) 2/3 - 5")

    def test_size_getter_setter(self):
        # Test the size getter and setter
        s = Square(5, 2, 3, 1)
        self.assertEqual(s.size, 5)

        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    # Add more tests as needed for other methods and edge cases

if __name__ == '__main__':
    unittest.main()
