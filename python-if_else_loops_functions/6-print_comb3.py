#!/usr/bin/python3
for num in range(0, 10):
    for pos in range(0, 10):
        if num >= pos:
            pass
        elif num == 8 and pos == 9:
            print("{}{}".format(num, pos))
        else:
            print("{}{}".format(num, pos), end=", ")
