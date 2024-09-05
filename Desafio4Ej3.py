import math
B = 20  
H = 0.3  
n = 0.03  
S = 0.0003  
f = (B * H)**(5/3) / (B + 2 * H)**(2/3)
    # Derivada parcial con respecto a n
par_n = -1 / n**2 * f * math.sqrt(S)
    # Derivada parcial con respecto a S
par_S = 1 / n * f * 1 / (2 * math.sqrt(S))
Q=f*(1/n)*math.sqrt(S)
print(Q)
deln=0.03*0.10
delS=0.0003*0.10
eq=abs(par_n)*deln+abs(par_S)*delS
print('derivada Parcial respecto n: ', par_n)
print('derivada Parcial respecto S: ', par_S)
print('error: ', eq)
print('entre: ',Q+eq,' y ',Q-eq)
