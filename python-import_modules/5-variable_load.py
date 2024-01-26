#!/usr/bin/python3
import importlib

if __name__ == "__main__":
    module_name = "variable_load_5"
    module = importlib.import_module(module_name)
    
    print(module.a)
