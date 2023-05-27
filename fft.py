import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.fft import fftfreq
from scipy.fft import fft, ifft, fft2, ifft2
import re

T = 40                              #seconds
N = 100                             #measurements
t = np.linspace(0, T, N)            #cria um vetor linear com espaçamentos iguais de N, de 0 a T
dt = np.diff(t)[0]                  #acha dt


#==============================================================================================#

## Fazendo leitura dos arquivos ##

#   1500 - 2000 - 2500 - 3000 - 3500 - 4000
#
#   data/ASSOALHO/x-ASSOALHO
#   data/CORTA FOGO/x-CORTAFOGO
#   data/MOTOR/x-MOTOR
#   data/PEDAL/x-PEDAL
#   data/VOLANTE/VOLANTE

file_path = 'data/ASSOALHO/2000-ASSOALHO.txt'

vetor_time  = []
vetor_x     = []
vetor_y     = []
vetor_z     = []

with open(file_path, 'r') as file:

    next(file) #pula a primeira linha

    for line in file:

            line = line.strip()

            if line : #checa se linha eh vazia

                time_aux = re.findall(r'[\d]+', line) #ta pegando todos os numeros, quero so o primeiro q aparece

                numbers = re.findall(r'[-]*[\d]*[.][\d]+', line)  #ok, acha todos os floats

                if len(numbers) < 3 :
                    numbers.append("0.00000")           #preenche vetor numbers quando não consegue index 3 na leitura com 0 (gambiarra)

                lista_float = [float (i) for i in time_aux] #cria uma lista de floats com os valores str de time_aux


                if len(lista_float) < 7 :                   #verifica os casos que falta ponto no numero float
                                                            #ou que nao possui o primeiro algarismo
                    for i in range(len(lista_float)) : 

                        if lista_float[i] > 1000 :

                            contador = 0
                            
                            while lista_float[i] > 0 :

                                lista_float[i] /= 10

                                contador += 1
                                if contador == 8 : break            #as vezes dava loop infinito (gambiarra)

                            
                            if i == 1 :
                                numbers[0] = lista_float[i]

                            if i == 3 :
                                numbers[1] = lista_float[i]

                            if i == 5 :
                                numbers[2] = lista_float[i]


                time = float(time_aux[0])
                x = float(numbers[0])
                y = float(numbers[1])
                z = float(numbers[2])

                vetor_time.append(time)
                vetor_x.append(x)
                vetor_y.append(y)
                vetor_z.append(z)



    print("Time:", vetor_time)
    print("X:", vetor_x)
    print("Y:", vetor_y)
    print("Z:", vetor_z)

