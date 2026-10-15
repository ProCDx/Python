# Arguments from Command Line
# Run:  python 38_arguments_from_command_line.py -c red

import sys
print("sys.argv:", sys.argv)   # list: [script name, arg1, arg2, ...]

# argparse is the better way
import argparse

parser = argparse.ArgumentParser(description="This program prints a color HEX value")
parser.add_argument("-c", "--color", metavar="color",
                    required=False, default="red",
                    choices={"red", "yellow"},
                    help="the color to search for")

args = parser.parse_args()
print(args.color)
