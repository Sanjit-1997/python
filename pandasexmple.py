import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("D:\python\country_wise_latest.csv")
df=loc.head(:,Confirmed,)
print(df)
df2=df.dropna()
print(df2)
df3=df.head(10)
print(df3)
print(df["Country/Region"])
plt.plot(df3["Confirmed"],df3["Country/Region"])
plt.plot(df3["Confirmed"],df3["Death"])
plt.show()
