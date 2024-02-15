import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

    def test_setters(self):
        r = Rectangle(1, 1, 1, 1, 1)

        with self.assertRaises(TypeError):
            r.width = "hello"
        with self.assertRaises(ValueError):
            r.width = 0

        with self.assertRaises(TypeError):
            r.height = "hello"
        with self.assertRaises(ValueError):
            r.height = 0

        with self.assertRaises(TypeError):
            r.x = "hello"
        with self.assertRaises(ValueError):
            r.x = -1

        with self.assertRaises(TypeError):
            r.y = "hello"
        with self.assertRaises(ValueError):
            r.y = -1

    def test_area(self):
        r = Rectangle(5, 3)
        self.assertEqual(r.area(), 15)

    def test_display(self):
        r = Rectangle(3, 3)
        r.display()

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 50)
        self.assertEqual(r.to_dictionary(), {'id': 50, 'width': 10, 'height': 2, 'x': 1, 'y': 9})

if __name__ == "__main__":
    unittest.main()
