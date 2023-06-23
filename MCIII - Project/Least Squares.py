import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])
y = np.array([1.59, 1.62, 0.70, 1.80, 2.76, 4.54, 4.64, 2.24, 5.47, -0.85, 3.25, 3.81, 3.01, 2.18, 
              1.90, -0.90, 0.19, 0.67, 1.06, 0.71, -0.85, 1.23, 6.08])

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