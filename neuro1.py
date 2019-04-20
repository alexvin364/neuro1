import matplotlib.pyplot as plt
import numpy as np
import os

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
    if (ed==0):
        print(output, end = ", ")
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
    count = 0
    print("\nResult:  ", end = "")
    if (learn == "all"):
        for i in range(16):
            count += iteration(answer[i],inputs[i],0)
        for j in range(16):
            iteration(answer[j],inputs[j],1)
    else:
        if (activationNum == "1"):
            for i in (3,7,11,12):
                count += iteration(answer[i],inputs[i],0)
            for i in (3,7,11,12):
                iteration(answer[i],inputs[i],1)
        else:
            for i in (3,12,15):
                count += iteration(answer[i],inputs[i],0)
            for i in (3,12,15):
                iteration(answer[i],inputs[i],1)
    print("\nE =", count)
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
y = np.array([])

os.system("cls")
activationNum = input("Enter activation function number (type 1 or 2)\n")
while (activationNum == "1" or activationNum == "2"):
    learn = input('Enter "all" or "min"\n')
    if (learn!="all") and (learn!="min"): break
    i=0
    while (i<=30):
        print("\nPeriod #",i,"\nWeights: ", end = "")
        for weight in weights: print(round(weight,3), end = ", ")
        i+=1
        err = period()
        y = np.append(y,np.array([err]))
        if (err==0):
            break
    if (learn=="min"):   #проверка
        print("\nChecking the learning results:")
        learn="all"
        period()
    
    x = np.arange(i)                            #построение графика
    fig = plt.figure()
    plt.axis([0, i, 0, max(y)+1])
    plt.plot(x, y)
    plt.grid(True)
    fig.canvas.set_window_title('Mistakes over generations')
    plt.xlabel('generations')
    plt.ylabel('number of mistakes')
    print("\n\n================Close graph to continue================")
    plt.show()
    weights = np.array([0.0,0.0,0.0,0.0,0.0]).T
    y = np.array([])
    os.system("cls")
    activationNum = input("Enter activation function number (type 1 or 2)\n")
    
