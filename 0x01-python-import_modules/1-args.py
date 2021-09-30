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

    for arg in range(1, total):
            print("{}: {}".format(arg, sys.argv[arg]))
            sys.argv[i]

if __name__ == "__main__":
    main()
