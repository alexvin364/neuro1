import numpy as np

def activation1(net):                           #пороговая ФА
    if (net>=0): return 1
    else: return 0

def activation2(net):                           #ФА №2
    if ((1 + net/(1+abs(net)))/2 >=0.5): return 1
    else: return 0

def iteration(realOutput,inputs,ed):               #предъявление на вход и проверка
    net = np.dot(weights,inputs)
    if (activationNum == "1"):
        output = activation1(net)
    else:
        output = activation2(net)
    delta = realOutput - output
    if (delta==0):
        mistake = 0
    else:
        mistake = 1
    if (ed==1):
        for i in range(5):
            if (activationNum == "1"):
                weights[i] += norma*delta*inputs[i]
            else:
                weights[i] += norma*delta*inputs[i]/((1+abs(net)*(1+abs(net))))
    return mistake

def period():                                   #эпоха обучения, считает ошибки
    num = 0
    count = 0
    if (learn == "all"):
        for i in range(16):
            count += iteration(answer[num],inputs[i],0)
            num+=1
    else:
        for i in (z1,z2,z3,z4):
            count += iteration(answer[i],inputs[i],0)
        for i in (z1,z2,z3,z4):
            iteration(answer[i],inputs[i],1)
    return count

inputs = []
for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            for x4 in range(2):
                inputs.append([1,x1,x2,x3,x4])

norma = 0.3                                     #начальные данные
answer = np.array([1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0])
weights = np.array([0.0,0.0,0.0,0.0,0.0]).T

activationNum = input("Enter activation function number (type 1 or 2)\n")
for z4 in range(16):
    for z3 in range(16):
        for z2 in range(16):
            for z1 in range(16):
                learn = "min"
                for i in range(30):
                    err = period()
                    if (err==0):
                        break
                learn="all"
                s = period()
                weights = np.array([0.0,0.0,0.0,0.0,0.0]).T
                y = np.array([])
                if (s == 0) and (z1<z2) and (z2<z3):
                    print(z1,z2,z3,z4)
