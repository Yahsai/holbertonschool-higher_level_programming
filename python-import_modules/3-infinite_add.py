#!/usr/bin/python3
if __name__ == "__main__":
    import sys

ac = len(sys.argv)
if ac == 1:
    print("0")
else:
    sum = 0
    for j in range(1, ac):
        sum += int(sys.argv[j])
    print("{}".format(sum))