import pandas as pd


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