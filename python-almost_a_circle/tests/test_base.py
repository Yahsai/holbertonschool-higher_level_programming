import unittest
import json
import os
from models.base import Base

class TestBase(unittest.TestCase):
    def test_init(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(5)
        self.assertEqual(b3.id, 5)

    def test_to_json_string(self):
        obj = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        json_str = Base.to_json_string(obj)
        expected_str = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        self.assertEqual(json_str, expected_str)

    def test_save_to_file(self):
        obj_list = [Base(1), Base(2), Base(3)]
        Base.save_to_file(obj_list)
        filename = "Base.json"
        with open(filename, "r") as file:
            content = file.read()
            expected_content = '[{"id": 1}, {"id": 2}, {"id": 3}]'
            self.assertEqual(content, expected_content)

    def test_from_json_string(self):
        json_str = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        obj_list = Base.from_json_string(json_str)
        expected_list = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        self.assertEqual(obj_list, expected_list)

    def test_create(self):
        dictionary = {"id": 5, "name": "Charlie"}
        obj = Base.create(**dictionary)
        self.assertEqual(obj.id, 5)
        self.assertEqual(obj.name, "Charlie")

    def test_load_from_file(self):
        obj_list = [Base(1), Base(2), Base(3)]
        Base.save_to_file(obj_list)
        loaded_list = Base.load_from_file()
        self.assertEqual(len(loaded_list), 3)
        self.assertEqual(loaded_list[0].id, 1)
        self.assertEqual(loaded_list[1].id, 2)
        self.assertEqual(loaded_list[2].id, 3)

    def test_draw(self):
        # Add your draw method tests if needed
        pass

if __name__ == "__main__":
    unittest.main()
