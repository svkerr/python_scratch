# Reference: http://karpathy.github.io/neuralnets/-2,3

import numpy as np
from numpy import random

def forwardMultiplyGate(x,y):
  return(x * y)

x = -2; y = 3	# some input values
h = 0.0001
out = forwardMultiplyGate(x,y)

# Strategy 2
# Let's compute Numerical Derivatives instead of guessing an x,y pair
# Compute the derivative of f with respect to x
xph = x + h
out2 = forwardMultiplyGate(xph,y)
x_deriv = (out2 - out)/h

# Compute the derivative of f with respect to y
yph = y + h
out3 = forwardMultiplyGate(x,yph)
y_deriv = (out3 - out)/h

print(out, out2, out3, x_deriv, y_deriv)

# Now take gradient and add back to inputs using step_size (i.e., learning rate)
step_size = 0.01

x = x + step_size * x_deriv
y = y + step_size * y_deriv
out_new = forwardMultiplyGate(x,y)

print(x, y, out_new)
# Excellent - using numerical gradient beats a random guess
# Note: The gradient is the direction of the steepest ascent of the function
# But the numerical gradient is computationally expensive

# Strategy 3
## Recursive Cases: The Chain Rule and Backpropagation
# f(x,y,z) = (x+y)z 

def forwardMultiplyGate2(a,b):
  return(a * b)

def forwardAddGate(a,b):
  return(a + b)

def forwardCircuit(x,y,z):
  q = forwardAddGate(x,y)
  f = forwardMultiplyGate2(q,z)
  return(f)

x=-2; y=5; z=-4

f = forwardCircuit(x,y,z)
print(f)

# Now for backpropagation and the Chain Rule


