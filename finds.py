import pandas as pd

df=pd.read_csv('data.csv')
data=df.values.tolist()

num_attribrutes = len(data[0])-1
hypothesis = [''] * num_attribrutes


for example in data:
  if example[-1].lower()=='yes':
    for i in range(num_attribrutes):
      if hypothesis[i]=='':
        hypothesis[i]=example[i]
      elif hypothesis[i]!=example[i]:
        hypothesis[i]='?'


print("Final Hypothesis : ",hypothesis)

