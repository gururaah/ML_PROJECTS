import numpy as np
import pandas as pd 
from sklearn import linear_model
import matplotlib.pyplot as plt
import math

df=pd.read_csv('house_price_pre_mul.csv')
#print(df)
#print(df.bedroom.median())
df.bedroom=df.bedroom.fillna(df.bedroom.median())
#print(df)

new_df=df.drop('price',axis=1)
#print(new_df)

mod1=linear_model.LinearRegression()
mod1.fit(new_df,df.price)
sqrt_foot=float(input('enter square foot : '))
house_age=float(input('enter house age : '))
bedroom=float(input('enter no of bed : '))
s=mod1.predict(pd.DataFrame([[sqrt_foot,bedroom,house_age]],columns=new_df.columns))
if s<0:
    print('No available house within the given criteria.')
else:
 print('price of house is : rs',s)