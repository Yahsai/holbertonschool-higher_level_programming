import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_init(self):
        s1 = Square(5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(2, 2)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s2.width, 2)
        self.assertEqual(s2.height, 2)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 0)

        s3 = Square(3, 1, 3, 12)
        self.assertEqual(s3.id, 12)
        self.assertEqual(s3.size, 3)
        self.assertEqual(s3.width, 3)
        self.assertEqual(s3.height, 3)
        self.assertEqual(s3.x, 1)
        self.assertEqual(s3.y, 3)

    def test_setters(self):
        s = Square(1, 1, 1, 1)

        with self.assertRaises(TypeError):
            s.size = "hello"
        with self.assertRaises(ValueError):
            s.size = 0

        with self.assertRaises(TypeError):
            s.x = "hello"
        with self.assertRaises(ValueError):
            s.x = -1

        with self.assertRaises(TypeError):
            s.y = "hello"
        with self.assertRaises(ValueError):
            s.y = -1

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_display(self):
        s = Square(3)
        s.display()

    def test_str(self):
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 4")

    def test_update(self):
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual(str(s), "[Square] (89) 10/10 - 10")
        s.update(89, 2)
        self.assertEqual(str(s), "[Square] (89) 10/10 - 2")
        s.update(89, 2, 3)
        self.assertEqual(str(s), "[Square] (89) 10/10 - 2")
        s.update(89, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (89) 4/10 - 2")
        s.update(89, 2, 3, 4, 5)
        self.assertEqual(str(s), "[Square] (89) 4/5 - 2")

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 50)
        self.assertEqual(s.to_dictionary(), {'id': 50, 'size': 10, 'x': 2, 'y': 1})

if __name__ == "__main__":
    unittest.main()
