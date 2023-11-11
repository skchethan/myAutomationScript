"""Imports print_error and print_success functions from outputColoring module.

These functions are used to print messages to console in different colors.

The main() function demonstrates using the imported functions."""

from outputColoring import print_error, print_success

def main():
    print("This script is being run to test the colour import module")
    print_error("ERROR")
    print_success("SUCCESS")

if __name__ == '__main__':
    main()