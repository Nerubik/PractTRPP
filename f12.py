x=287
import math
def f12(x):
    if x<116:
        res=40*pow((math.tan(x)-pow(x,6)),5)+pow(x,3)
    elif x>=116 and x<205:
        res=math.sin(math.sin(22*pow(x,2)))-70*pow(x,8)
    elif x>=205 and x<260:
        res=pow(x,6)-pow(x,8)
    elif x>=260 and x<296:
        res=pow(x,7)-math.fabs(x)+99
    else:
        res=90*(52*pow(x,2)-pow(x,4)+90)-pow(math.e,x)
    return res
f12(x)

    
