import math
import numpy as np
import random
import scipy.stats as ss
from pylab import *


def Get_sample(sample_num):
    x=[]
    y=[]
    space=1.0/(sample_num-1)
    for i in range(sample_num):
        x.append(i*space)
        append_num=np.sin(i*space*2*pi)+np.random.normal(0,1)/5
        y.append(append_num)
    return x,y

def Least_square(x,y,degree):
    x_arr=[]
    sam_num=len(x)
    for i in range(sam_num):
        x_tem_arr=[]
        for j in range(degree+1):
            x_tem=x[i]**(degree-j)
            x_tem_arr.append(x_tem)
        x_arr.append(x_tem_arr)
    x_mat=mat(x_arr)
    y_mat=mat(y).T
    xTx=x_mat.T*x_mat
    pl=(xTx.I)*(x_mat.T*y_mat)
    return pl

def Regularized_least_square(x,y,degree,numda):
    x_arr=[]
    sam_num=len(x)
    for i in range(sam_num):
        x_tem_arr=[]
        for j in range(degree+1):
            x_tem=x[i]**(degree-j)
            x_tem_arr.append(x_tem)
        x_arr.append(x_tem_arr)
    x_mat=mat(x_arr)
    y_mat=mat(y).T
    xTx=x_mat.T*x_mat
    n=len(xTx)
    I=np.identity(n)
    pl=(xTx.I-numda*I)*(x_mat.T*y_mat)
    return pl

def Least_square_test(degree,sample_num):
    draw_sin()
    x,y=Get_sample(sample_num)
    draw_sample(x,y)
    pl=Least_square(x,y,degree)
    draw_reg(pl)
    show()


def Regularized_least_square_test(degree,sample_num,lnnumda):
    draw_sin()
    x,y=Get_sample(sample_num)
    draw_sample(x,y)
    numda=2.718**(lnnumda)
    pl=Regularized_least_square(x,y,degree,numda)
    draw_reg(pl)
    show()

def draw_sin():
    x=np.linspace(0,1,250,endpoint=True)
    y=np.sin(np.pi*x*2)
    xticks([0,1])
    yticks([-1,0,1])
    plot(x,y)

def draw_reg(pl):
    xx=np.linspace(0,1,250)
    plot(xx,polyval(pl,xx),'r-')

def draw_sample(x,y):
    plot(x,y,'o')

Least_square_test(3,10)
Least_square_test(9,10)
Least_square_test(9,15)
Least_square_test(9,100)
Regularized_least_square_test(9,10,-18)









        
        
