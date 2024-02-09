#!/usr/bin/python3
def class_to_json(obj):
    """
    Convert an object to a JSON-serializable dictionary.

    Args:
    - obj: An instance of a class with serializable attributes (list, dictionary, string, integer, and boolean).

    Returns:
    - A dictionary representing the serialized form of the object.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("Input object must be an instance of a class")

    serializable_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_dict[key] = value
        elif isinstance(value, MyClass):  # Handle nested objects of type MyClass
            serializable_dict[key] = class_to_json(value)
        elif value is None:
            serializable_dict[key] = None
        else:
            raise TypeError(f"Attribute '{key}' has an unsupported type: {type(value).__name__}")

    return serializable_dict

# Assuming your MyClass definition is in a module named '8-my_class'
class MyClass:
    def __init__(self, name, number=0):
        self.__name = name
        self.number = number
        self.is_team_red = (self.number % 2) == 0
        self.score = 0

    def win(self):
        self.score += 1

    def lose(self):
        self.score -= 1

    def __str__(self):
        return "[MyClass] {} - {:d} => {:d}".format(self.__name, self.number, self.score)

# Example usage
if __name__ == "__main__":
    m = MyClass("John")
    m.win()

    print(type(m))
    print(m)

    mj = class_to_json(m)
    print(type(mj))
    print(mj)

