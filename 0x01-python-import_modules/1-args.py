#!/usr/bin/python3

import sys

def main(*argv):
    i = 0
    total = len(sys.argv)

    for args in sys.argv:
        if (i != 0):
            print("{}: {}".format(i, args))
            i = i + 1
    # Take this out of the for loop?
        if total == 1:
            print("{:d} argument:".format(total))
        elif total == 0:
            print("{:d} argument:".format(total))
        else:
            print("{:d} argument:".format(total))

if __name__ == "__main__":
    main()
