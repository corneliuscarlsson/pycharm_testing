# if _a=None_ == '__main__':
import matplotlib.pyplot as plt
import numpy as np


# TODO: Fix Bug
# TODO: Implement Tests
print("Pycharm is Awesome")
x = np.arange(0, 4 * np.pi, 0.1)
y = np.cos(x)

plt.plot(x, y)
plt.show()

def add(a, b):
    c = a + b
    return c


print(add(2, 3))