import pandas as pd 
import numpy as np 
from sklearn import linear_model
import matplotlib.pyplot as plt 
df=pd.read_csv('room_price.csv')
#print(df)

plt.xlabel('area')
plt.ylabel('price')
plt.scatter(df.area,df.price,color='red',marker="*")
#plt.show()

new_df=df.drop('price',axis=1)
#print(new_df)
model1=linear_model.LinearRegression()
model1.fit(new_df,df.price,)
p=model1.predict(pd.DataFrame([[50000]],columns=new_df.columns))
#print(p)
#plt.show()
area_df=pd.read_csv('areas.csv')
#print(area_df)
s=model1.predict(area_df)
print(s)
area_df['price']=s
area_df.to_csv('areas_output.csv')