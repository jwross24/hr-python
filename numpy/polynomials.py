# You are given the coefficients of a polynomial P.
#
# Your task is to find the value of P at point x.

import numpy

coefficients = [float(e) for e in input().split(' ')]
x = float(input())

print(numpy.polyval(coefficients, x))
