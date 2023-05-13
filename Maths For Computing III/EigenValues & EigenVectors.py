import numpy as np
import matplotlib.pyplot as plt

n = 9
v1 = [4, 3]
v2 = [-4, 1]

xkList = []

for k in range(n):
    for i in range(0,2):
        xk = 3.445 * pow(1.2, k) * v1[i] + (-0.32) * pow((-0.4), k) * v2[i]
        xkList.append(round(xk))

jk = []
ak = []
plus = []
divide = []

for count, items in enumerate(xkList):
    if count % 2 == 0:
        jk.append(items)
    else:
        ak.append(items)

for items in range(n):
    plus.append(jk[items] + ak[items])
    divide.append(jk[items] / ak[items])

plt.plot(jk, '.', label = "j(k)")
plt.plot(ak, '.', label = "a(k)")
plt.plot(plus, '.', label = "j(k) + a(k)")
plt.plot(divide, '.', label = "j(k) / a(k)")
plt.yticks(np.arange(0, 110, 10))
plt.xlabel('k')
plt.ylabel(plt.legend())
plt.grid()
plt.show()