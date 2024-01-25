#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if ord(char) >= 97 and ord(char) <= 122:
            upper_char = chr(ord(char) - 32)
            print("{}".format(upper_char), end='')
        else:
            print("{}".format(char), end='')
