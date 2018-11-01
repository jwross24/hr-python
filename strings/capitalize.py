#!/bin/python3

import os


# Complete the solve function below.
def solve(s):
    string = s.capitalize()  # for loop doesn't take care of first character
    result = ''
    for i in range(len(string)):
        if string[0].isspace() and string[1].islower():
                result += string[0]
                string = string[1:].capitalize()
        else:
            result += string[0]
            string = string[1:]
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
