import numpy as np


def gread_desrnt(x,y):
    m_curr=b_curr=0
    itera=1000
    n=len(x)
    l_rate=0.08
    for i in range(itera):
        yp=m_curr*x+b_curr

        cost=(1/n)*sum([j**2 for j in (y-yp)])
        md=-(2/n)*sum(x*(y-yp))
        bd=-(2/n)*sum(y-yp)

        m_curr= m_curr-l_rate*md
        b_curr=b_curr-l_rate*bd
        print("m  {} ,     b  {}     ,cost  {},     iter {}".format(m_curr,b_curr,cost,i))
    pass
        






x=np.array([1,2,3,4,5])
y=np.array([5,7,9,11,13])

gread_desrnt(x,y)
