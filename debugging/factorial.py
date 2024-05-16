#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    try:
        f = factorial(int(sys.argv[1]))
        print(f)
    except IndexError:
        print("Error: No input provided. Please provide an integer.")
    except ValueError:
        print("Error: Invalid input. Please provide a valid integer.")
