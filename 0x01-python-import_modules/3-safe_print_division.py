#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        ouput = a/b   
    except ZeroDivisionError:
        output = None

    finally:
        print("Inside result: {}".format(output))
    return output
