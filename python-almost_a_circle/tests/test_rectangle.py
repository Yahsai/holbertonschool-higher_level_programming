import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):

    def test_rectangle__init(self):
        r1 = Rectangle(10, 7, 2, 8)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 7)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 8)

        r2 = Rectangle(5, 5)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        with self.assertRaises(ValueError):
            r3 = Rectangle(0, 5)

        with self.assertRaises(TypeError):
            r4 = Rectangle(5, "height")

    def test_area(self):
        r1 = Rectangle(3, 5)
        self.assertEqual(r1.area(), 15)

        r2 = Rectangle(7, 4)
        self.assertEqual(r2.area(), 28)

    def test_display(self):
        r1 = Rectangle(2, 3)
        expected_output = "  ##\n  ##\n  ##\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r1.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        r2 = Rectangle(2, 2, 1, 1)
        expected_output = "\n ##\n ##\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r2.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1, 0, 10)
        self.assertEqual(str(r2), "[Rectangle] (10) 1/0 - 5/5")

    def test_update(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        r1.update(13, 7, 8, 3, 4)
        self.assertEqual(r1.id, 13)
        self.assertEqual(r1.width, 7)
        self.assertEqual(r1.height, 8)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

        r2 = Rectangle(5, 5, 1, 0, 10)
        r2.update(width=2, x=2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.x, 2)

    def test_to_dictionary(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        expected_dict = {'id': 12, 'width': 4, 'height': 6, 'x': 2, 'y': 1}
        self.assertEqual(r1.to_dictionary(), expected_dict)

        r2 = Rectangle(5, 5, 1, 0, 10)
        expected_dict = {'id': 10, 'width': 5, 'height': 5, 'x': 1, 'y': 0}
        self.assertEqual(r2.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
