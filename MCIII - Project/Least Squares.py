import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([0.67, 1.06, 0.71, -0.85, 1.23, 6.08])

A = np.vstack([x, np.ones(len(x))]).T

m, c = np.linalg.lstsq(A, y, rcond=None)[0]

plt.plot(x, y, 'o', label='Original data', markersize=10)
plt.plot(x, m*x + c, 'r', label='Fitted line')
plt.legend()
plt.xlabel('Year')
plt.ylabel('Inflation, consumer prices (annual %)')
plt.grid()
plt.title('Thailand')
plt.show()

