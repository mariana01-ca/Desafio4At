import math
'Variables x0 y x1'
x0=1
x1=2.5

c=1
h=x1-x0

sum=0
p1=math.log(x0)
sum+=p1
s=1
c=1
while c<=4:
    if c==2 or c==1:
        ex=1
    else:
        ex=ex*(c-1)
    t=ex*math.pow(h,c)/math.pow(x0,c)
    t1=round(t/math.factorial(c),2)
    sum=round(sum+s*t1,2)
    er=round(abs((math.log(x1)-sum)/math.log(x1))*100,2)
    print('aproximacion: ',sum,' error: ',t1,' error relativo: ',er, '%')
    s=s*-1
    c+=1

print('Valor verdadero de IN(2.5)', math.log(x1))    


