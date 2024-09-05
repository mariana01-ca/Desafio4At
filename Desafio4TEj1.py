import math
x0=1
x1=3

t1=25
t2=-6
t3=7
t4=88
p1= t1*math.pow(x0,3)+t2*math.pow(x0,2)+t3*x0-t4
p2= t1*math.pow(x1,3)+t2*math.pow(x1,2)+t3*x1-t4
c=3
sum=0
sum=sum+p1
h=x1-x0
ex=1
print('valor real: ',p2)
print('Valor Aproximado   ','ef: ', '    error relativo: ' )
while(c!=0):
    t1=c*t1*math.pow(x0,c-1)
    t2=(c-1)*t2*math.pow(x0,c-2)
    k=((t1+t2+t3)*math.pow(h,ex))/math.factorial(ex)
    sum=sum+k
    er=round(((p2-sum)/p2)*100,3)
    print('   ',sum, '          ',k, '    ',er,' %' )    
    if(c-2==0):
        t2=0
    if(c==3):
        t3=0    
    c-=1
    ex+=1