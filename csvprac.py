import pandas as pd
df=pd.read_csv("D:\python\Dataset.csv")
#print(df.to_string())
dfnew=df.head(10)
print(dfnew)
df2=dfnew['age']
print(df2)
for x in df2.index:
    if df2.loc[x]<3:
        df2.loc[x]=3
print(df2)
