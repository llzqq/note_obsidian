#! /usr/bin/env python3
import numpy as np
import matplotlib.pylab as plt

def step_function(x):
  return np.array(x>0, dtype=np.int)

def sigmoid_function(x):
  return 1/(1+np.exp(-x))

def ReLU_function(x):
  return np.maximum(0, x)

x = np.arange(-5.0, 5.0, 0.1)
y1 = step_function(x)
y2 = sigmoid_function(x)
y3 = ReLU_function(x)

if __name__ == "__main__":
  plt.plot(x, y1)
  plt.plot(x, y2)
  plt.plot(x, y3)
  plt.ylim(-0.1, 1.1)
  plt.show()
