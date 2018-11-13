import numpy

coefficients = [float(e) for e in input().split(' ')]
x_value = float(input())

print(numpy.polyval(coefficients, x_value))
