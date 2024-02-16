import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os


class TestBase(unittest.TestCase):

    def test_base__init(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_to_json_string(self):
        list_dicts = [{'id': 1, 'x': 2, 'y': 3}, {'id': 4, 'x': 5, 'y': 6}]
        json_string = Base.to_json_string(list_dicts)
        expected_result = json.dumps(list_dicts)
        self.assertEqual(json_string, expected_result)

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)

        filename = "Rectangle.json"
        with open(filename, "r") as file:
            content = file.read()
            expected_content = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8},' \
                               ' {"x": 0, "width": 2, "id": 2, "height": 4, "y": 0}]'
            self.assertEqual(content, expected_content)

        # Clean up after the test
        os.remove(filename)

    def test_from_json_string(self):
        json_string = '[{"id": 1, "x": 2, "y": 3}, {"id": 4, "x": 5, "y": 6}]'
        list_dicts = Base.from_json_string(json_string)
        expected_result = [{'id': 1, 'x': 2, 'y': 3}, {'id': 4, 'x': 5, 'y': 6}]
        self.assertEqual(list_dicts, expected_result)

    def test_create(self):
        dictionary = {'id': 1, 'x': 2, 'y': 3}
        dummy_instance = Base.create(**dictionary)
        self.assertIsInstance(dummy_instance, Base)
        self.assertEqual(dummy_instance.id, 1)
        self.assertEqual(dummy_instance.x, 2)
        self.assertEqual(dummy_instance.y, 3)

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(len(list_rectangles_output), 2)
        self.assertIsInstance(list_rectangles_output[0], Rectangle)
        self.assertIsInstance(list_rectangles_output[1], Rectangle)

        # Clean up after the test
        os.remove("Rectangle.json")

    # Add more tests for other methods as needed

if __name__ == '__main__':
    unittest.main()
