import matplotlib.pyplot as plt
from scipy import stats

x = [100, 120, 150, 150, 180, 200, 250]
y = [85, 95, 115, 125, 140, 155, 180]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
print(myfunc(225))
plt.show()
