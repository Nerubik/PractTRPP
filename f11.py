import math
x= 83
y= -51
z= -91
def f11 (x,y,z):
    res= ((40*pow(y,4)+62*pow(z,6))/(72*pow(x,6)+math.sin(x)+59))-(((pow(y,2))/22)+math.log(x))/(pow(x,6)-15*pow(x,8))-(pow(z,7)-(pow(y,6)/5))
    return res
f11 (x,y,z)
