import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_init_with_id(self):
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_init_without_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_to_json_string_empty_list(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_non_empty_list(self):
        result = Base.to_json_string([{'id': 1, 'name': 'object1'}, {'id': 2, 'name': 'object2'}])
        expected = '[{"id": 1, "name": "object1"}, {"id": 2, "name": "object2"}]'
        self.assertEqual(result, expected)

    def test_save_to_file(self):
        pass

    def test_from_json_string_empty_string(self):
        result = Base.from_json_string("")
        self.assertEqual(result, [])

    def test_from_json_string_non_empty_string(self):
        json_string = '[{"id": 1, "name": "object1"}, {"id": 2, "name": "object2"}]'
        result = Base.from_json_string(json_string)
        expected = [{'id': 1, 'name': 'object1'}, {'id': 2, 'name': 'object2'}]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

