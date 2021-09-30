#!/usr/bin/python3

import sys

def main(*argv):
    i = 0
    total = len(sys.argv)

    if total == 1:
        print("{:d} arguments:".format(total - 1))
    elif total == 2:
        print("{:d} argument:".format(total - 1))
    else:
        print("{:d} arguments:".format(total - 1))

    for args in sys.argv:
        if (i != 0):
            print("{}: {}".format(i, args))
            i = i + 1

if __name__ == "__main__":
    main()
