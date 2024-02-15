import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init(self):
        # Test the constructor
        r = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_str(self):
        # Test the __str__ method
        r = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 2/3 - 5/10")

    def test_width_getter_setter(self):
        # Test the width getter and setter
        r = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(r.width, 5)

        r.width = 15
        self.assertEqual(r.width, 15)

    # Add more tests as needed for other methods and edge cases

if __name__ == '__main__':
    unittest.main()
