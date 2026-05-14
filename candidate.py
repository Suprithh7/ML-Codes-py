import pandas as pd

df=pd.read_csv('data.csv')
data=df.values.tolist()

num_attributes = len(data[0])-1

S= ['']*num_attributes
G =[['?']*num_attributes]


def is_consistent(h,x):
  for i in range(len(h)):
    if h[i]!='?' and h[i]!=x[i]:
      return False
  return True


for example in data:
  x= example[:-1]
  label = example[-1]

  if label.lower()=='yes':
    G=[g for g in G if is_consistent(g,x)]
    for i in range(num_attributes):
      if S[i]=='':
        S[i]=x[i]
      elif S[i]!=x[i]:
        S[i]='?'

  else:
    new_G=[]
    for g in G:
      if is_consistent(g,x):
        for i in range(num_attributes):
          if g[i]=='?':
            if S[i]!=x[i]:
              new_h=g.copy()
              new_h[i]=x[i]
              new_G.append(new_h)
    G= new_G


print(S)
print(G)




