import pandas as pd
df=pd.read_csv("rainfall in india 1901-2015.csv")
df.head()
kerala=df[df.SUBDIVISION=="KERALA"]
print(len(kerala))
print(kerala.loc[kerala.ANNUAL.idxmax(),["YEAR","ANNUAL"]])
print(kerala[["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]].mean())
avg=kerala.ANNUAL.mean()
print(avg)
print((kerala.ANNUAL>avg).sum())