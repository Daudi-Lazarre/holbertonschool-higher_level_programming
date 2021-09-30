#!/usr/bin/python3

import sys

def main(*argv):
    i = 0
    total = len(sys.argv)

# I over-hyped this problem.
# Do total - 1 to shift numbers back to start at zero.
# ... because total does not start a 0th index???

    if total == 1:
        print("{:d} arguments:".format(total - 1))
    elif total == 2:
        print("{:d} argument:".format(total - 1))
    else:
        print("{:d} arguments:".format(total - 1))

# Nvm, why is this printing the file and not the output after it?
# I was printing the wrong variable

    for arg in range(1, total):
            print("{}: {}".format(arg, sys.argv[arg]))
            sys.argv[i]

if __name__ == "__main__":
    main()
