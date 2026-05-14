import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('california_housing.csv')
data=df.values.tolist()

x = [row[0] for row in data]
y = [row[-1] for row in data]

n=len(x)


sum_x=sum(x)
sum_y=sum(y)
sum_xy=sum(x[i]*y[i] for i in range(n))
sum_x2 = sum(x[i]**2 for i in range(n))

m = (n*sum_xy-sum_x*sum_y)/(n*sum_x2-sum_x**2)
c = (sum_y - m*sum_x)/n


print("slope:",m)
print("intercept: ",c)


def predict(x_val):
  return m*x_val + c

print("x = 6",predict(6))

plt.figure(figsize=(10, 6))

# 1. Plot actual data
plt.scatter(x, y, color='blue', alpha=0.5, s=20, label='Data')

# 2. Plot regression line
x_min, x_max = min(x), max(x)
y_min, y_max = m * x_min + c, m * x_max + c
plt.plot([x_min, x_max], [y_min, y_max], color='red', linewidth=2, label='Line')

# 3. Labels
plt.xlabel('X (Feature)', fontsize=12)
plt.ylabel('Y (Target)', fontsize=12)
plt.title(f'Linear Regression: y = {m:.4f}x + {c:.4f}', fontsize=13, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.savefig('linear_regression.png')
plt.show()