k = float(input("Insira a constante térmica: ")) # Entrada de dados - Constante do material
n = float(input("Insira o número de subdivisões: ")) # Entrada de dados - Para determinar os intervalos de tempo (Quanto maior, mais preciso)
tf =float(input("Insira o tempo final: ")) # Entrada de dados - Tempo o qual a temperatura será determinada
ti =float(input("Insira o tempo inicial: ")) # Entrada de dados - Tempo inicial do problema
T0 = float(input("Insira a temperatura inicial: ")) # Entrada de dados - Temperatura inicial do corpo
Tm = float(input("Digite a temperatura final (ambiente): ")) # Entrada de dados - Temperatura final (Temperatura do ambiente)

#---------- Função para o cálculo do passo da variável tempo ----------
def calcpasso(ite):
    return ((tf-ti)/ite)
#----------------------------------------------------------------------

#---------- Função para o cálculo das inclinações das retas de aproximação ----------
def dTdt(Temp):
    incli = -k*(Temp-Tm) # Inclinação da reta aproximada, para a lei de resfriamento de Newton
    return incli
#-------------------------------------------------------------------------------------
    
#---------- Método de euler ----------
def metodoeuler(Temperatura,tempo):
    i = 0
    while n>i:
        inc = dTdt(Temperatura) # Cálculo da inclinação
        Temperatura =  Temperatura+(passo*inc) # Cálculo da nova temperatura, de acordo com o coeficiente angular obtido no passo anterior
        tempo = tempo + passo # atualização do tempo
        i = i+1 # variável de controle de iterações
    return Temperatura    
#--------------------------------------

#---------- Corpo do programa principal ----------
passo = calcpasso(n)
Tfinal = 0
Tfinal = metodoeuler(T0,ti)
print("A temperatura final é: %.5fºC " % Tfinal)
#-------------------------------------------------
