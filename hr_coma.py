import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df=pd.read_csv('HR_comma_sep.csv')
#print(df.head())

#data visuliz
pd.crosstab(df.salary,df.left).plot(kind='bar')
#print(plt.show())

bf=df[['satisfaction_level','average_montly_hours','promotion_last_5years','salary']]
cf=pd.get_dummies(bf.salary)
#print(cf.head())

sf=pd.concat([bf,cf],axis=1)
sf=sf.drop(['salary'],axis=1)
#print(sf.head())

x_train,x_test,y_train,y_test=train_test_split(sf,df.left,test_size=0.2)

model1=LogisticRegression()
q=model1.fit(x_train,y_train)
m=q.predict(x_test)
print(m)
#print(q.score(x_test,y_test))