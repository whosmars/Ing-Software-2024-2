import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = x**3

# Plot the function
plt.plot(x, y, label='$f(x) = x^3$')
plt.title('Funcion Cubica: $f(x) = x^3$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()