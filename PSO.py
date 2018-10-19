# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 15:48:23 2018

@author: leodflag
"""
import random,math
import numpy as np
import matplotlib.pyplot as plt
#v=速率，x=位置，t=時間，s=距離
#-------------初始位置-------------
XXX=[]  #母體
x_range=[]
X0=[]
X1=[]
Xmax=100

#-------------初始速度-------------
VVV=[]  #母體
v_range=[]  #母體
V0=[]
V1=[]
Vmax=200

N=10 #N為粒子數

Z=[] #Z為最佳函數(極小化)
z=0.0
ALL=[]
itera=300
w=0.9-(0.5/itera)
c0=2.0
c1=2.0
pltX=[]
pltY=[]

one_best=[]
group_best=[]


#-----------初始位置-------------
def init_p(N):
    global x_range
    for i in range(N):
        X0.append(random.uniform(-100,100))
        X1.append(random.uniform(-100,100))
    x_range=list(zip(X0,X1))
    return x_range

##-----------初始速度-------------
def init_v(N):
    global v_range
    for i in range(N):
        V0.append(random.uniform(-4,4))
        V1.append(random.uniform(-4,4))
    v_range=list(zip(V0,V1))
    return v_range
            
#-------------適應函數-------------
def adapt_fun(x,v,N):
    global x_range,v_range,ALL,group_best
    X0[:],X1[:]=zip(*x)
    V0[:],V1[:]=zip(*v)
    for i in range(N):
        z=X0[i]*X0[i]+2*X1[i]*X1[i]-0.3*math.cos(3*math.pi*X0[i]) \
            -0.4*math.cos(4*math.pi*X1[i])+0.7
        Z.append(z)
    x_range=list(zip(X0,X1))
    v_range=list(zip(V0,V1))
    ALL=list(zip(Z,x_range,v_range))
    del Z[0:N]
    
    return ALL

#-------------判斷速度-------------
def VRange(V):
    for k in range(N):
        if V[k]>Vmax:
            V[k]=Vmax
        elif V[k]<-Vmax :
            V[k]=-Vmax
        else:
            V[k]
    return V

#-------------判斷位置-------------
def XRange(X):
    for k in range(N):
        if X[k]>Xmax:
            X[k]=Xmax
        elif X[k]<-Xmax :
            X[k]=-Xmax
        else:
            X[k]
    return X

"""
繪圖函數
"""
def plotData(plt, data):
    x = [p[0] for p in data]
    y = [p[1] for p in data]
    plt.plot(x, y)

#------------主程式開始------------
#---------------初始化---------    
XXX=init_p(N)  
VVV=init_v(N)
XXX=list(zip(X0,X1))
VVV=list(zip(V0,V1))    
ALL=adapt_fun(XXX,VVV,N)
group_best=sorted(ALL)[0]
one_best=ALL
while(itera>0):
    #-------------計算適應值-------------
    XXX=list(zip(X0,X1))
    VVV=list(zip(V0,V1))    
    ALL=adapt_fun(XXX,VVV,N)

    #-------------群體最佳值更新-------------
    for i in range(N):
        if ALL[i][0] > group_best[0] :
            group_best
        else:
            group_best=ALL[i]
            
    #-------------個體最佳值更新-------------
    
    for i in range(N):
        if ALL[i][0] < one_best[i][0]:
            one_best[i]=ALL[i]
        else:
            one_best

    #-------------速度更新-------------
    r0=random.random()
    r1=random.random()
    for i in range(N):
        V0[i]=w*V0[i]+c0*r0*(X0[i]-x_range[i][0])+c1*r1*(group_best[1][0]-x_range[i][0])
        V1[i]=w*V1[i]+c0*r0*(X1[i]-x_range[i][1])+c1*r1*(group_best[1][1]-x_range[i][1])

    #-------------速度調整-------------
        if V0[i]>100 or V0[i]<-100:
            VRange(V0)
        if V1[i]>100 or V1[i]<-100:
            VRange(V1)        

    #-------------位置更新-------------
    for i in range(N):    
        X0[i]=X0[i]+V0[i]
        X1[i]=X1[i]+V1[i]

    #-------------位置調整-------------
        if X0[i]>100 or X0[i]<-100:
            XRange(X0)
        if X1[i]>100 or X1[i]<-100:
            XRange(X1)
            
    print('group_best',group_best)
    pltY.append(group_best[0])
    pltX.append(150-itera)#圖的X軸為次數
    itera-=1
    
"""
繪圖
"""
geneChart=list(zip(pltX,pltY))
plotData(plt, geneChart)
plt.show()