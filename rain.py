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
print(kerala.isnull().sum())
kerala=kerala.dropna(subset=["ANNUAL"])
#dropping the years with missing annual rainfall data
kerala['DECADE']=kerala.YEAR//10 *10
print(kerala.groupby("DECADE").ANNUAL.mean())
kerala.to_csv("kerala_clean.csv",index=False)
print(kerala["ANNUAL"]) // returns the annual rainfall data for Kerala  
print(kerala[["ANNUAL"]])// returns the annual rainfall data for Kerala in a DataFrame format
